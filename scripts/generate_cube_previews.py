"""Generate 3-D hyperspectral-cube and ground-truth previews.

Every cube face is derived from the downloaded hyperspectral data. The front
face is a three-band composite; the top and right faces are colour-mapped
spectral cross-sections through the same cube. Source cubes are sampled in
memory and are never copied into the repository. Portrait scenes are rotated
for display, and each preview includes a numbered colour legend read from its
class-details page. README previews are rendered at 2x density for sharp text
and imagery on high-density displays.
"""

from __future__ import annotations

import argparse
import gc
import math
import re
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np
import scipy.io as sio
import tifffile
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

from generate_previews import PALETTE, fit, load_font, save_png


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = REPO_ROOT.parent / "HSI_data"


@dataclass(frozen=True)
class CubeSpec:
    name: str
    output_dir: str
    relative_path: str
    kind: str
    key: str | None
    shape: tuple[int, int, int]
    rgb_bands: tuple[int, int, int]


@dataclass
class SampledCube:
    data: np.ndarray
    band_indices: np.ndarray
    original_shape: tuple[int, int, int]


@dataclass(frozen=True)
class LegendGroup:
    title: str
    names: tuple[str, ...]


CUBE_SPECS = [
    CubeSpec(
        "Indian Pines",
        "Indian_Pines",
        "Indian_Pines/Indian_pines_corrected.mat",
        "mat",
        "indian_pines_corrected",
        (145, 145, 200),
        (29, 19, 9),
    ),
    CubeSpec(
        "Pavia University",
        "Pavia",
        "Pavia_University/PaviaU.mat",
        "mat",
        "paviaU",
        (610, 340, 103),
        (53, 29, 10),
    ),
    CubeSpec(
        "Pavia Centre",
        "Pavia_Centre",
        "Pavia_Centre/Pavia.mat",
        "mat",
        "pavia",
        (1096, 715, 102),
        (53, 29, 10),
    ),
    CubeSpec(
        "Salinas",
        "Salinas",
        "Salinas/Salinas_corrected.mat",
        "mat",
        "salinas_corrected",
        (512, 217, 204),
        (29, 19, 9),
    ),
    CubeSpec(
        "Kennedy Space Center",
        "KSC",
        "KSC/KSC.mat",
        "mat",
        "KSC",
        (512, 614, 176),
        (29, 19, 9),
    ),
    CubeSpec(
        "Botswana",
        "Botswana",
        "Botswana/Botswana.mat",
        "mat",
        "Botswana",
        (1476, 256, 145),
        (24, 14, 6),
    ),
    CubeSpec(
        "Houston 2013",
        "Houston",
        "Houston/Houstondata.mat",
        "mat",
        "Houstondata",
        (1905, 349, 144),
        (59, 40, 23),
    ),
    CubeSpec(
        "Trento",
        "Trento",
        "Trento/Italy_hsi.mat",
        "mat",
        "data",
        (166, 600, 63),
        (25, 14, 5),
    ),
    CubeSpec(
        "WHU-Hi-LongKou",
        "WHU-Hi-LongKou",
        "WHU-Hi-LongKou/WHU_Hi_LongKou.mat",
        "mat",
        "WHU_Hi_LongKou",
        (550, 400, 270),
        (112, 67, 31),
    ),
    CubeSpec(
        "WHU-Hi-HanChuan",
        "WHU-Hi-HanChuan",
        "WHU-Hi-HanChuan/WHU_Hi_HanChuan.mat",
        "mat",
        "WHU_Hi_HanChuan",
        (1217, 303, 274),
        (112, 67, 31),
    ),
    CubeSpec(
        "WHU-Hi-HongHu",
        "WHU-Hi-HongHu",
        "WHU-Hi-HongHu/WHU_Hi_HongHu.mat",
        "mat",
        "WHU_Hi_HongHu",
        (940, 475, 270),
        (112, 67, 31),
    ),
    CubeSpec(
        "Chikusei",
        "Chikusei",
        "Chikusei/Hyperspec_Chikusei_MATLAB/Chikusei_MATLAB/"
        "HyperspecVNIR_Chikusei_20140729.mat",
        "hdf5_mat",
        "chikusei",
        (2517, 2335, 128),
        (56, 36, 21),
    ),
    CubeSpec(
        "MUUFL Gulfport",
        "MUUFL_Gulfport",
        "MUUFL_Gulfport/muufl_gulfport_campus_1_hsi_220_label.mat",
        "muufl",
        None,
        (325, 220, 64),
        (29, 18, 9),
    ),
    CubeSpec(
        "Xiongan",
        "Xiongan",
        "Xiongan/Hyperspectral_XiongAn/Hyperspectral_XiongAn.img",
        "envi_bsq",
        None,
        (1580, 3750, 256),
        (119, 71, 35),
    ),
]


def sampling_steps(shape: tuple[int, int, int]) -> tuple[int, int, int]:
    rows, columns, bands = shape
    return (
        max(1, math.ceil(rows / 900)),
        max(1, math.ceil(columns / 900)),
        max(1, math.ceil(bands / 96)),
    )


def sample_array(array: np.ndarray, shape: tuple[int, int, int]) -> SampledCube:
    if tuple(array.shape) != shape:
        raise ValueError(f"Expected cube {shape}, received {array.shape}")
    row_step, column_step, band_step = sampling_steps(shape)
    sampled = np.asarray(
        array[::row_step, ::column_step, ::band_step], dtype=np.float32
    )
    return SampledCube(sampled, np.arange(0, shape[2], band_step), shape)


def load_cube(spec: CubeSpec, source_root: Path) -> SampledCube:
    path = source_root / spec.relative_path
    if spec.kind == "mat":
        payload = sio.loadmat(path, variable_names=[spec.key])
        full = np.asarray(payload[spec.key])
        sampled = sample_array(full, spec.shape)
        del full, payload
        gc.collect()
        return sampled

    if spec.kind == "hdf5_mat":
        row_step, column_step, band_step = sampling_steps(spec.shape)
        with h5py.File(path, "r") as handle:
            dataset = handle[spec.key]
            stored_shape = (spec.shape[2], spec.shape[1], spec.shape[0])
            if tuple(dataset.shape) != stored_shape:
                raise ValueError(f"Expected stored cube {stored_shape}, received {dataset.shape}")
            sampled = np.asarray(
                dataset[::band_step, ::column_step, ::row_step], dtype=np.float32
            ).transpose(2, 1, 0)
        return SampledCube(
            sampled,
            np.arange(0, spec.shape[2], band_step),
            spec.shape,
        )

    if spec.kind == "muufl":
        payload = sio.loadmat(path, simplify_cells=True)
        full = np.asarray(payload["hsi"]["Data"])
        sampled = sample_array(full, spec.shape)
        del full, payload
        gc.collect()
        return sampled

    if spec.kind == "envi_bsq":
        row_step, column_step, band_step = sampling_steps(spec.shape)
        rows, columns, bands = spec.shape
        full = np.memmap(
            path,
            dtype="<u2",
            mode="r",
            shape=(bands, rows, columns),
        )
        sampled = np.asarray(
            full[::band_step, ::row_step, ::column_step], dtype=np.float32
        ).transpose(1, 2, 0)
        del full
        return SampledCube(
            sampled,
            np.arange(0, bands, band_step),
            spec.shape,
        )

    if spec.kind == "tiff":
        full = tifffile.memmap(path)
        sampled = sample_array(full, spec.shape)
        del full
        return sampled

    raise ValueError(f"Unknown cube kind: {spec.kind}")


def rotate_for_display(cube: SampledCube) -> SampledCube:
    """Rotate portrait scenes so the spatial image remains readable on GitHub."""
    rows, columns, bands = cube.original_shape
    if rows <= columns * 1.25:
        return cube
    return SampledCube(
        np.rot90(cube.data, k=1, axes=(0, 1)),
        cube.band_indices,
        (columns, rows, bands),
    )


def needs_display_rotation(shape: tuple[int, int, int]) -> bool:
    return shape[0] > shape[1] * 1.25


def class_legend_groups(class_details_path: Path) -> list[LegendGroup]:
    groups: list[LegendGroup] = []
    title = "Classes"
    names: list[str] = []

    def finish_group() -> None:
        nonlocal names
        if names:
            groups.append(LegendGroup(title, tuple(names)))
            names = []

    for line in class_details_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            finish_group()
            section = line[3:].strip()
            if section == "Groundtruth.img":
                title = "Groundtruth classes"
            elif section == "Farm_roi.img":
                title = "Farm ROI classes"
            else:
                title = section
            continue
        match = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", line)
        if not match:
            continue
        class_id = int(match.group(1))
        if class_id != len(names) + 1:
            raise ValueError(
                f"Non-contiguous class IDs in {class_details_path}: "
                f"expected {len(names) + 1}, received {class_id}"
            )
        names.append(match.group(2).strip())
    finish_group()
    if not groups:
        raise ValueError(f"No class names found in {class_details_path}")
    return groups


def valid_values(array: np.ndarray) -> np.ndarray:
    values = array[np.isfinite(array)]
    positive = values[values > 0]
    if positive.size >= max(64, round(values.size * 0.2)):
        return positive
    return values


def normalise(array: np.ndarray) -> np.ndarray:
    values = valid_values(array)
    if values.size == 0:
        return np.zeros(array.shape, dtype=np.float32)
    low, high = np.percentile(values, (1.0, 99.0))
    if not np.isfinite(low) or not np.isfinite(high) or high <= low:
        low, high = float(values.min()), float(values.max())
    if high <= low:
        return np.zeros(array.shape, dtype=np.float32)
    scaled = (np.asarray(array, dtype=np.float32) - low) / (high - low)
    return np.clip(np.nan_to_num(scaled), 0.0, 1.0)


def rgb_composite(cube: SampledCube, bands: tuple[int, int, int]) -> Image.Image:
    positions = [int(np.argmin(np.abs(cube.band_indices - band))) for band in bands]
    channels = [np.power(normalise(cube.data[:, :, position]), 0.88) for position in positions]
    rgb = np.stack(channels, axis=2)
    image = Image.fromarray(np.rint(rgb * 255).astype(np.uint8), mode="RGB")
    image = ImageEnhance.Contrast(image).enhance(1.06)
    return ImageEnhance.Color(image).enhance(1.10)


def spectral_colours(array: np.ndarray) -> Image.Image:
    scaled = normalise(array)
    stops = np.array([0.0, 0.18, 0.38, 0.58, 0.78, 1.0])
    colours = np.array(
        [
            [23, 28, 54],
            [50, 77, 173],
            [34, 169, 184],
            [114, 203, 91],
            [250, 196, 55],
            [197, 48, 67],
        ],
        dtype=np.float32,
    )
    channels = [np.interp(scaled, stops, colours[:, index]) for index in range(3)]
    rgb = np.stack(channels, axis=2).astype(np.uint8)
    return Image.fromarray(rgb, mode="RGB")


def shear_top(image: Image.Image, depth_x: int) -> Image.Image:
    width, height = image.size
    result = Image.new("RGBA", (width + depth_x, height), (0, 0, 0, 0))
    denominator = max(1, height - 1)
    for y in range(height):
        shift = round(depth_x * (1 - y / denominator))
        result.paste(image.crop((0, y, width, y + 1)), (shift, y))
    return result


def shear_right(image: Image.Image, depth_y: int) -> Image.Image:
    width, height = image.size
    result = Image.new("RGBA", (width, height + depth_y), (0, 0, 0, 0))
    denominator = max(1, width - 1)
    for x in range(width):
        shift = round(depth_y * (1 - x / denominator))
        result.paste(image.crop((x, 0, x + 1, height)), (x, shift))
    return result


def render_cube(
    cube: SampledCube,
    rgb_bands: tuple[int, int, int],
    canvas_size: tuple[int, int] = (1800, 940),
    max_front: tuple[int, int] = (1400, 720),
    depth: tuple[int, int] = (280, 150),
) -> Image.Image:
    canvas_width, canvas_height = canvas_size
    maximum_width, maximum_height = max_front
    depth_x, depth_y = depth
    rows, columns, _ = cube.original_shape
    ratio = min(maximum_width / columns, maximum_height / rows)
    front_width = max(84, round(columns * ratio))
    front_height = max(84, round(rows * ratio))

    front = rgb_composite(cube, rgb_bands).resize(
        (front_width, front_height), Image.Resampling.LANCZOS
    )
    centre_row = cube.data.shape[0] // 2
    centre_column = cube.data.shape[1] // 2
    top_source = spectral_colours(cube.data[centre_row, :, :].T).resize(
        (front_width, depth_y), Image.Resampling.BILINEAR
    )
    right_source = spectral_colours(cube.data[:, centre_column, :]).resize(
        (depth_x, front_height), Image.Resampling.BILINEAR
    )
    top = shear_top(top_source, depth_x)
    right = shear_right(right_source, depth_y)

    total_width = front_width + depth_x
    total_height = front_height + depth_y
    left = max(16, (canvas_width - total_width) // 2)
    front_top = max(depth_y + 16, (canvas_height - total_height) // 2 + depth_y)

    canvas = Image.new("RGBA", canvas_size, "#f7f8fa")
    shadow = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        (
            left + 10,
            front_top - depth_y + 16,
            left + total_width + 20,
            front_top + front_height + 26,
        ),
        radius=20,
        fill=(21, 31, 50, 42),
    )
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
    canvas.alpha_composite(top, (left, front_top - depth_y))
    canvas.alpha_composite(right, (left + front_width, front_top - depth_y))
    canvas.alpha_composite(front.convert("RGBA"), (left, front_top))

    draw = ImageDraw.Draw(canvas)
    edge = "#243149"
    draw.line(
        [
            (left, front_top),
            (left + depth_x, front_top - depth_y),
            (left + front_width + depth_x, front_top - depth_y),
            (left + front_width, front_top),
            (left, front_top),
        ],
        fill=edge,
        width=4,
        joint="curve",
    )
    draw.line(
        [
            (left + front_width, front_top),
            (left + front_width + depth_x, front_top - depth_y),
            (left + front_width + depth_x, front_top + front_height - depth_y),
            (left + front_width, front_top + front_height),
            (left + front_width, front_top),
        ],
        fill=edge,
        width=4,
        joint="curve",
    )
    draw.rectangle(
        (
            left,
            front_top,
            left + front_width - 1,
            front_top + front_height - 1,
        ),
        outline=edge,
        width=4,
    )
    return canvas.convert("RGB")


def render_hyrank(source_root: Path) -> Image.Image:
    root = source_root / "HyRANK/HyRANK_satellite/HyRANK_satellite/TrainingSet"
    dioni_spec = CubeSpec(
        "Dioni", "HyRANK", str(root / "Dioni.tif"), "tiff", None,
        (250, 1376, 176), (24, 14, 6)
    )
    loukia_spec = CubeSpec(
        "Loukia", "HyRANK", str(root / "Loukia.tif"), "tiff", None,
        (249, 945, 176), (24, 14, 6)
    )

    def load_absolute(spec: CubeSpec) -> SampledCube:
        full = tifffile.memmap(Path(spec.relative_path))
        sampled = sample_array(full, spec.shape)
        del full
        return sampled

    dioni = load_absolute(dioni_spec)
    loukia = load_absolute(loukia_spec)
    canvas = Image.new("RGB", (1800, 940), "#f7f8fa")
    title_font = load_font(40, bold=True)
    for cube, spec, y in ((dioni, dioni_spec, 50), (loukia, loukia_spec, 494)):
        rendered = render_cube(
            cube,
            spec.rgb_bands,
            canvas_size=(1680, 390),
            max_front=(1380, 244),
            depth=(240, 104),
        )
        canvas.paste(rendered, (60, y))
        draw = ImageDraw.Draw(canvas)
        draw.text((80, y + 10), spec.name, fill="#172033", font=title_font)
    return canvas


def ground_truth_panel(
    output_root: Path,
    rotate: bool,
    size: tuple[int, int] = (1415, 750),
) -> Image.Image:
    if output_root.name == "HyRANK":
        items = [
            ("Dioni", output_root / "dioni_gt.png"),
            ("Loukia", output_root / "loukia_gt.png"),
        ]
    elif output_root.name == "Xiongan":
        items = [
            ("Groundtruth", output_root / "gt.png"),
            ("Farm ROI", output_root / "farm_roi.png"),
        ]
    else:
        items = [("", output_root / "gt.png")]

    panel = Image.new("RGB", size, "#f7f8fa")
    if len(items) == 1:
        with Image.open(items[0][1]) as source:
            image = source.convert("RGB")
        if rotate:
            image = image.transpose(Image.Transpose.ROTATE_90)
        fitted = fit(image, size[0] - 32, size[1] - 32)
        panel.paste(
            fitted,
            ((size[0] - fitted.width) // 2, (size[1] - fitted.height) // 2),
        )
        return panel

    draw = ImageDraw.Draw(panel)
    title_font = load_font(38, bold=True)
    title_height = 48
    gap = 20
    outer_margin = 12
    slot_height = (
        size[1]
        - outer_margin * 2
        - len(items) * title_height
        - (len(items) - 1) * gap
    ) // len(items)
    y = outer_margin
    for item_index, (title, path) in enumerate(items):
        bounds = draw.textbbox((0, 0), title, font=title_font)
        title_width = bounds[2] - bounds[0]
        draw.text(
            ((size[0] - title_width) / 2, y),
            title,
            fill="#172033",
            font=title_font,
        )
        y += title_height
        with Image.open(path) as source:
            image = source.convert("RGB")
        fitted = fit(image, size[0] - 32, slot_height)
        panel.paste(
            fitted,
            ((size[0] - fitted.width) // 2, y + (slot_height - fitted.height) // 2),
        )
        y += slot_height
        if item_index < len(items) - 1:
            y += gap
    return panel


def palette_rgb(class_id: int) -> tuple[int, int, int]:
    colour = PALETTE[class_id].lstrip("#")
    return tuple(int(colour[index : index + 2], 16) for index in (0, 2, 4))


def legend_columns(group: LegendGroup) -> int:
    return 4 if len(group.names) >= 20 else 3


def legend_group_height(group: LegendGroup) -> int:
    rows = math.ceil(len(group.names) / legend_columns(group))
    return 120 + rows * 90


def render_legends(groups: list[LegendGroup], width: int = 3000) -> Image.Image:
    gap = 24
    height = sum(legend_group_height(group) for group in groups) + gap * (len(groups) - 1)
    canvas = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(canvas)
    heading_font = load_font(58, bold=True)
    label_font = load_font(50)
    number_font = load_font(36, bold=True)
    y = 0

    for group in groups:
        group_height = legend_group_height(group)
        draw.rounded_rectangle(
            (40, y, width - 40, y + group_height - 4),
            radius=28,
            fill="#f7f8fa",
            outline="#d8dde8",
            width=4,
        )
        draw.text((80, y + 28), group.title, fill="#172033", font=heading_font)
        columns = legend_columns(group)
        column_width = (width - 160) // columns
        item_y = y + 112
        swatch_size = 64
        for index, name in enumerate(group.names):
            row, column = divmod(index, columns)
            class_id = index + 1
            x = 80 + column * column_width
            top = item_y + row * 90
            colour = palette_rgb(class_id)
            draw.rounded_rectangle(
                (x, top, x + swatch_size, top + swatch_size),
                radius=8,
                fill=colour,
                outline="#4a5568",
                width=2,
            )
            luminance = 0.2126 * colour[0] + 0.7152 * colour[1] + 0.0722 * colour[2]
            number_colour = "#ffffff" if luminance < 135 else "#172033"
            number = str(class_id)
            bounds = draw.textbbox((0, 0), number, font=number_font)
            draw.text(
                (
                    x + (swatch_size - (bounds[2] - bounds[0])) / 2,
                    top + (swatch_size - (bounds[3] - bounds[1])) / 2 - 2,
                ),
                number,
                fill=number_colour,
                font=number_font,
            )
            draw.text(
                (x + swatch_size + 18, top + 5),
                name,
                fill="#172033",
                font=label_font,
            )
        y += group_height + gap
    return canvas


def combined_preview(
    cube: Image.Image,
    output_root: Path,
    rotate_labels: bool,
    legend_groups: list[LegendGroup],
) -> Image.Image:
    legends = render_legends(legend_groups)
    canvas = Image.new("RGB", (3000, 950 + legends.height), "#ffffff")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(64, bold=True)
    cards = ((30, 90, 1485, 900), (1515, 90, 2970, 900))
    for card in cards:
        draw.rounded_rectangle(card, radius=28, fill="#f7f8fa", outline="#d8dde8", width=4)

    for title, centre in (("Hyperspectral cube", 758), ("Ground truth", 2243)):
        bounds = draw.textbbox((0, 0), title, font=title_font)
        width = bounds[2] - bounds[0]
        draw.text((centre - width / 2, 18), title, fill="#172033", font=title_font)

    cube_ratio = min(1415 / cube.width, 750 / cube.height)
    cube_size = (
        max(1, round(cube.width * cube_ratio)),
        max(1, round(cube.height * cube_ratio)),
    )
    cube_fitted = cube.resize(cube_size, Image.Resampling.LANCZOS)
    cube_position = (
        50 + (1415 - cube_fitted.width) // 2,
        115 + (750 - cube_fitted.height) // 2,
    )
    canvas.paste(cube_fitted, cube_position)
    labels = ground_truth_panel(output_root, rotate_labels)
    canvas.paste(labels, (1535, 115))
    canvas.paste(legends, (0, 930))
    return canvas


def build(source_root: Path) -> None:
    for spec in CUBE_SPECS:
        cube = load_cube(spec, source_root)
        display_cube = rotate_for_display(cube)
        rendered = render_cube(display_cube, spec.rgb_bands)
        output_root = REPO_ROOT / "data" / spec.output_dir
        legend_groups = class_legend_groups(output_root / "Class_details.md")
        save_png(rendered, output_root / "cube.png")
        save_png(
            combined_preview(
                rendered,
                output_root,
                needs_display_rotation(spec.shape),
                legend_groups,
            ),
            output_root / "preview.png",
        )
        print(f"{spec.name}: {spec.shape[0]} x {spec.shape[1]} x {spec.shape[2]}")
        del cube, display_cube, rendered
        gc.collect()

    hyrank = render_hyrank(source_root)
    hyrank_root = REPO_ROOT / "data/HyRANK"
    hyrank_legends = class_legend_groups(hyrank_root / "Class_details.md")
    save_png(hyrank, hyrank_root / "cube.png")
    save_png(
        combined_preview(hyrank, hyrank_root, False, hyrank_legends),
        hyrank_root / "preview.png",
    )
    print("HyRANK: Dioni and Loukia")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        default=DEFAULT_SOURCE_ROOT,
        help="Directory containing the downloaded HSI_data folders",
    )
    args = parser.parse_args()
    build(args.source_root.resolve())


if __name__ == "__main__":
    main()
