"""Generate consistent ground-truth previews from locally downloaded datasets.

The script reads label rasters only. It never copies hyperspectral cubes into this
repository. Pixel values are preserved; nearest-neighbour resizing is used solely
for compact PNG previews.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import scipy.io as sio
import tifffile
from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = REPO_ROOT.parent / "HSI_data"

# Background plus 22 visually distinct class colours. Colours are presentation
# metadata only; the class identifiers in the source rasters are not changed.
PALETTE = [
    "#f4f5f7",
    "#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabed4",
    "#469990", "#dcbeff", "#9a6324", "#fffac8", "#800000",
    "#aaffc3", "#808000", "#ffd8b1", "#000075", "#a9a9a9",
    "#000000", "#7fdbff",
]


@dataclass(frozen=True)
class Preview:
    name: str
    output_dir: str
    label: np.ndarray
    labeled_pixels: int


def matlab_array(path: Path, key: str) -> np.ndarray:
    return np.asarray(sio.loadmat(path)[key])


def muufl_labels(path: Path) -> np.ndarray:
    data = sio.loadmat(path, simplify_cells=True)
    return np.asarray(data["hsi"]["sceneLabels"]["labels"])


def chikusei_labels(path: Path) -> np.ndarray:
    data = sio.loadmat(path, simplify_cells=True)
    return np.asarray(data["GT"]["gt"])


def xiongan_labels(path: Path) -> np.ndarray:
    return np.fromfile(path, dtype=np.uint8).reshape(1580, 3750)


def colour_table() -> list[int]:
    values: list[int] = []
    for colour in PALETTE:
        colour = colour.lstrip("#")
        values.extend(int(colour[index : index + 2], 16) for index in (0, 2, 4))
    values.extend([0] * (768 - len(values)))
    return values


def render_label(label: np.ndarray, max_side: int = 960) -> Image.Image:
    if label.ndim != 2:
        raise ValueError(f"Expected a 2-D label raster, received {label.shape}")
    label = label.copy()
    label[label < 0] = 0
    if label.max() >= len(PALETTE):
        raise ValueError(f"Label values {label.min()}..{label.max()} exceed the palette")

    image = Image.fromarray(label.astype(np.uint8), mode="P")
    image.putpalette(colour_table())
    longest = max(image.size)
    scale = min(max_side / longest, max(1.0, 600 / longest))
    if abs(scale - 1.0) > 0.001:
        size = tuple(max(1, round(value * scale)) for value in image.size)
        image = image.resize(size, Image.Resampling.NEAREST)
    return image.convert("RGB")


def save_png(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", optimize=True)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def fit(image: Image.Image, width: int, height: int) -> Image.Image:
    ratio = min(width / image.width, height / image.height)
    size = (max(1, round(image.width * ratio)), max(1, round(image.height * ratio)))
    return image.resize(size, Image.Resampling.NEAREST)


def paired_preview(left: Image.Image, right: Image.Image) -> Image.Image:
    canvas = Image.new("RGB", (1200, 470), "#ffffff")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(28, bold=True)
    for image, title, x in ((left, "Dioni", 30), (right, "Loukia", 615)):
        fitted = fit(image, 555, 385)
        canvas.paste(fitted, (x + (555 - fitted.width) // 2, 55 + (385 - fitted.height) // 2))
        box = draw.textbbox((0, 0), title, font=title_font)
        draw.text((x + (555 - (box[2] - box[0])) / 2, 14), title, fill="#172033", font=title_font)
    return canvas


def overview(previews: list[tuple[Preview, Image.Image]]) -> Image.Image:
    columns, rows = 3, 5
    tile_width, tile_height = 520, 285
    margin, gap = 36, 18
    canvas = Image.new(
        "RGB",
        (
            margin * 2 + columns * tile_width + (columns - 1) * gap,
            margin * 2 + rows * tile_height + (rows - 1) * gap,
        ),
        "#eef1f6",
    )
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(27, bold=True)
    note_font = load_font(20)

    for index, (preview, image) in enumerate(previews):
        row, column = divmod(index, columns)
        x = margin + column * (tile_width + gap)
        y = margin + row * (tile_height + gap)
        draw.rounded_rectangle(
            (x, y, x + tile_width, y + tile_height),
            radius=18,
            fill="#ffffff",
            outline="#d8dde8",
            width=2,
        )
        draw.text((x + 22, y + 16), preview.name, fill="#172033", font=title_font)
        note = f"{preview.labeled_pixels:,} labeled pixels"
        draw.text((x + 22, y + tile_height - 40), note, fill="#596579", font=note_font)
        fitted = fit(image, tile_width - 44, tile_height - 100)
        canvas.paste(
            fitted,
            (x + (tile_width - fitted.width) // 2, y + 55 + (tile_height - 105 - fitted.height) // 2),
        )
    return canvas


def build(source_root: Path) -> None:
    simple_sources = [
        ("Indian Pines", "Indian_Pines", "Indian_Pines/Indian_pines_gt.mat", "indian_pines_gt"),
        ("Pavia University", "Pavia", "Pavia_University/PaviaU_gt.mat", "paviaU_gt"),
        ("Pavia Centre", "Pavia_Centre", "Pavia_Centre/Pavia_gt.mat", "pavia_gt"),
        ("Salinas", "Salinas", "Salinas/Salinas_gt.mat", "salinas_gt"),
        ("Kennedy Space Center", "KSC", "KSC/KSC_gt.mat", "KSC_gt"),
        ("Botswana", "Botswana", "Botswana/Botswana_gt.mat", "Botswana_gt"),
        ("Houston 2013", "Houston", "Houston/Houstonlabel.mat", "Houstonlabel"),
        ("Trento", "Trento", "Trento/allgrd.mat", "mask_test"),
        ("WHU-Hi-LongKou", "WHU-Hi-LongKou", "WHU-Hi-LongKou/WHU_Hi_LongKou_gt.mat", "WHU_Hi_LongKou_gt"),
        ("WHU-Hi-HanChuan", "WHU-Hi-HanChuan", "WHU-Hi-HanChuan/WHU_Hi_HanChuan_gt.mat", "WHU_Hi_HanChuan_gt"),
        ("WHU-Hi-HongHu", "WHU-Hi-HongHu", "WHU-Hi-HongHu/WHU_Hi_HongHu_gt.mat", "WHU_Hi_HongHu_gt"),
    ]
    previews: list[Preview] = []
    for name, output_dir, relative_path, key in simple_sources:
        label = matlab_array(source_root / relative_path, key)
        previews.append(Preview(name, output_dir, label, int(np.count_nonzero(label))))

    chikusei = chikusei_labels(
        source_root
        / "Chikusei/Hyperspec_Chikusei_MATLAB/Chikusei_MATLAB/"
        / "HyperspecVNIR_Chikusei_20140729_Ground_Truth.mat"
    )
    previews.append(Preview("Chikusei", "Chikusei", chikusei, int(np.count_nonzero(chikusei))))

    hyrank_root = source_root / "HyRANK/HyRANK_satellite/HyRANK_satellite/TrainingSet"
    dioni = tifffile.imread(hyrank_root / "Dioni_GT.tif")
    loukia = tifffile.imread(hyrank_root / "Loukia_GT.tif")
    hyrank_count = int(np.count_nonzero(dioni) + np.count_nonzero(loukia))

    muufl = muufl_labels(source_root / "MUUFL_Gulfport/muufl_gulfport_campus_1_hsi_220_label.mat")
    previews.append(Preview("MUUFL Gulfport", "MUUFL_Gulfport", muufl, int(np.count_nonzero(muufl > 0))))

    xiongan_root = source_root / "Xiongan/ROI_GroundTruth"
    xiongan = xiongan_labels(xiongan_root / "Groundtruth.img")
    xiongan_farm = xiongan_labels(xiongan_root / "Farm_roi.img")
    previews.append(Preview("Xiongan", "Xiongan", xiongan, int(np.count_nonzero(xiongan))))

    rendered: list[tuple[Preview, Image.Image]] = []
    for preview in previews:
        image = render_label(preview.label)
        save_png(image, REPO_ROOT / "data" / preview.output_dir / "gt.png")
        rendered.append((preview, image))

    dioni_image = render_label(dioni)
    loukia_image = render_label(loukia)
    save_png(dioni_image, REPO_ROOT / "data/HyRANK/dioni_gt.png")
    save_png(loukia_image, REPO_ROOT / "data/HyRANK/loukia_gt.png")
    hyrank_image = paired_preview(dioni_image, loukia_image)
    save_png(hyrank_image, REPO_ROOT / "data/HyRANK/gt.png")
    hyrank_preview = Preview("HyRANK (Dioni + Loukia)", "HyRANK", dioni, hyrank_count)
    rendered.insert(13, (hyrank_preview, hyrank_image))

    save_png(render_label(xiongan_farm), REPO_ROOT / "data/Xiongan/farm_roi.png")
    save_png(overview(rendered), REPO_ROOT / "assets/catalog-overview.png")

    for preview, _ in rendered:
        print(f"{preview.name}: {preview.labeled_pixels:,}")


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
