<div align="center">

# Hyperspectral Image Datasets Collection

**Source index, file specifications, label statistics, and previews for 15 hyperspectral classification datasets**

[中文](../README.md) · [Sources and citations](SOURCES.md) · [Class statistics](#ground-truth-previews)

</div>

![Overview of 15 datasets](../assets/catalog-overview.png)

## Scope

This repository catalogs dataset metadata, primary sources, required citations, per-class pixel counts, and Ground Truth previews. The hyperspectral cubes are not committed to Git.

- Descriptions are limited to facts supported by a primary data page, an author-maintained project, a paper, or inspected package metadata.
- Spatial dimensions use **rows × columns**; cube dimensions use **rows × columns × bands**.
- Labeled-pixel counts are computed from the distributed GT files with background excluded.
- Primary sources, papers, and community mirrors are identified separately.
- See [SOURCES.md](SOURCES.md) for provenance, citation requirements, usage terms, and package discrepancies.

## Downloads

| Entry | Purpose | Status |
|---|---|---|
| [Quark Drive](https://pan.quark.cn/s/27a871c79b27) | Regional mirror for mainland China | HSI_data directory used for this revision; refer to the live folder for its actual contents |
| [Google Drive](https://drive.google.com/drive/folders/1xgSyrXw2NwzOUVaZ2BK1KBzgCDPKYC_n?usp=drive_link) | Backup mirror | Historical entry; its contents may lag behind the Quark mirror |
| “Source / paper” in the catalog below | Original data, current documentation, and citation terms | **Preferred entry** |

> Mirrors improve access only. They do not replace primary sources or grant redistribution rights. Obtain datasets that require a request, questionnaire, or restricted use from the official source and follow its terms.

## Dataset catalog

Specifications were checked against primary pages and the downloaded packages. The bands column gives the distributed file first and retains the raw-sensor or source-record count in parentheses where relevant.

| # | Dataset | Platform / sensor | Distributed shape | GSD | Classes / labeled pixels | Source / paper |
|---:|---|---|---|---:|---:|---|
| 1 | [Indian Pines](../data/Indian_Pines/Class_details.md) | Airborne AVIRIS | 145 × 145 × 220; corrected cube has 200 bands | 20 m | 16 / 10,249 | [Purdue](https://engineering.purdue.edu/~biehl/MultiSpec/hyperspectral.html) · [PURR](https://doi.org/10.4231/R7RX991C) |
| 2 | [Pavia University](../data/Pavia/Class_details.md) | Airborne ROSIS | 610 × 340 × 103 | 1.3 m | 9 / 42,776 | [UPV/EHU](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) |
| 3 | [Pavia Centre](../data/Pavia_Centre/Class_details.md) | Airborne ROSIS | 1096 × 715 × 102 | 1.3 m | 9 / 148,152 | [UPV/EHU](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) |
| 4 | [Salinas](../data/Salinas/Class_details.md) | Airborne AVIRIS | 512 × 217 × 204 (224 raw) | 3.7 m | 16 / 54,129 | [UPV/EHU](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) · [AVIRIS 1998](https://aviris.jpl.nasa.gov/ql/listla98.html) |
| 5 | [Kennedy Space Center](../data/KSC/Class_details.md) | Airborne AVIRIS | 512 × 614 × 176 (224 raw) | 18 m | 13 / 5,211 | [UPV/EHU](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) |
| 6 | [Botswana](../data/Botswana/Class_details.md) | EO-1 Hyperion | 1476 × 256 × 145 (242 raw) | 30 m | 14 / 3,248 | [UPV/EHU](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) |
| 7 | [Houston 2013](../data/Houston/Class_details.md) | Airborne CASI + LiDAR | 1905 × 349 × 144 | 2.5 m | 15 / 15,029 | [IEEE GRSS](https://www.grss-ieee.org/community/technical-committees/2013-ieee-grss-data-fusion-contest/) · [paper](https://doi.org/10.1109/JSTARS.2014.2305441) |
| 8 | [Trento](../data/Trento/Class_details.md) | AISA Eagle + Optech ALTM 3100EA | 166 × 600 × 63 + LiDAR | 1 m | 6 / 30,214 | [paper](https://doi.org/10.1109/JSTARS.2016.2634863) · [community mirror](https://github.com/tyust-dayu/Trento) |
| 9 | [WHU-Hi-LongKou](../data/WHU-Hi-LongKou/Class_details.md) | UAV / Headwall Nano-Hyperspec | 550 × 400 × 270 | 0.463 m | 9 / 204,542 | [WHU RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) · [paper](https://doi.org/10.1016/j.rse.2020.112012) |
| 10 | [WHU-Hi-HanChuan](../data/WHU-Hi-HanChuan/Class_details.md) | UAV / Headwall Nano-Hyperspec | 1217 × 303 × 274 | 0.109 m | 16 / 257,530 | [WHU RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) · [paper](https://doi.org/10.1016/j.rse.2020.112012) |
| 11 | [WHU-Hi-HongHu](../data/WHU-Hi-HongHu/Class_details.md) | UAV / Headwall Nano-Hyperspec | 940 × 475 × 270 | 0.043 m | 22 / 386,693 | [WHU RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) · [paper](https://doi.org/10.1016/j.rse.2020.112012) |
| 12 | [Chikusei](../data/Chikusei/Class_details.md) | Headwall Hyperspec-VNIR-C | 2517 × 2335 × 128 | 2.5 m | 19 / 77,592 | [author data page](https://naotoyokoya.com/Download.html) · SAL-2016-05-27 |
| 13 | [HyRANK](../data/HyRANK/Class_details.md) | EO-1 Hyperion | 5 scenes, 176 bands each | 30 m | 14-class taxonomy / 33,527¹ | [dataset DOI](https://doi.org/10.5281/zenodo.1222202) · [ISPRS report](https://www.isprs.org/society/si/SI-2017/ISPRS-SI2017-TC3_WG4_Karantzalos_Report.pdf) |
| 14 | [MUUFL Gulfport](../data/MUUFL_Gulfport/Class_details.md) | CASI-1500 + LiDAR | 325 × 220 × 64 + LiDAR² | 1 m² | 11 / 53,687 | [GatorSense / UF](https://github.com/GatorSense/MUUFLGulfport) · [label report](https://ufdc.ufl.edu/IR00009711/00001) |
| 15 | [Xiongan](../data/Xiongan/Class_details.md) | Airborne AMMIS VNIR | 1580 × 3750 × 256³ | 0.5 m | 19³ / 3,341,881 | [dataset DOI](https://doi.org/10.3974/geodb.2021.01.02.V1) · [paper](https://doi.org/10.11834/jrs.20209065) |

1. Public GT is distributed for the Dioni and Loukia HyRANK scenes. Their combined count is 33,527; Dioni contains 12 of the 14 taxonomy classes and Loukia contains all 14.
2. The local MUUFL package is the 1 m, 64-usable-band Campus 1 variant. Its metadata records the original 0.5 m, 72-band image.
3. The Xiongan data record states 250 effective bands and 19 land-cover types. The downloaded header states 256 bands and the package contains a 19-class Groundtruth map plus a 20-class Farm_roi map. Both observations are retained on the [class page](../data/Xiongan/Class_details.md).

## Source-supported acquisition facts

| Dataset | Acquisition time / location |
|---|---|
| Indian Pines | 12 June 1992; Indian Pine Test Site, Tippecanoe County, Indiana, USA |
| KSC | 23 March 1996; Kennedy Space Center, Florida, USA |
| Botswana | 31 May 2001; Okavango Delta, Botswana |
| Houston 2013 | LiDAR: 22 June 2012; HSI: 23 June 2012; University of Houston and the neighboring urban area |
| WHU-Hi-LongKou | 17 July 2018, 13:49–14:37; Longkou Town, Hubei, China |
| WHU-Hi-HanChuan | 17 June 2016, 17:57–18:46; Hanchuan, Hubei, China |
| WHU-Hi-HongHu | 20 November 2017, 16:23–17:37; Honghu City, Hubei, China |
| Chikusei | 29 July 2014, 09:56–10:53 (UTC+9); Chikusei, Ibaraki, Japan |
| MUUFL Gulfport | 8 November 2010; University of Southern Mississippi Gulf Park campus, Long Beach, Mississippi, USA |
| Xiongan | 3 October 2017, 15:40–16:03; Matiwan Village, Xiongan New Area, Hebei, China |
| Pavia University / Centre, Salinas, Trento, HyRANK | No single unambiguous acquisition date was verified from the linked primary source, so this catalog does not supply an inferred date |

## Ground Truth previews

Preview colors distinguish class identifiers only; label values are unchanged. Select a name for source labels and exact per-class counts.

<table>
<tr>
<td align="center"><a href="../data/Indian_Pines/Class_details.md"><img src="../data/Indian_Pines/gt.png" width="260" alt="Indian Pines ground truth"><br>Indian Pines</a></td>
<td align="center"><a href="../data/Pavia/Class_details.md"><img src="../data/Pavia/gt.png" width="260" alt="Pavia University ground truth"><br>Pavia University</a></td>
<td align="center"><a href="../data/Pavia_Centre/Class_details.md"><img src="../data/Pavia_Centre/gt.png" width="260" alt="Pavia Centre ground truth"><br>Pavia Centre</a></td>
</tr>
<tr>
<td align="center"><a href="../data/Salinas/Class_details.md"><img src="../data/Salinas/gt.png" width="260" alt="Salinas ground truth"><br>Salinas</a></td>
<td align="center"><a href="../data/KSC/Class_details.md"><img src="../data/KSC/gt.png" width="260" alt="KSC ground truth"><br>Kennedy Space Center</a></td>
<td align="center"><a href="../data/Botswana/Class_details.md"><img src="../data/Botswana/gt.png" width="260" alt="Botswana ground truth"><br>Botswana</a></td>
</tr>
<tr>
<td align="center"><a href="../data/Houston/Class_details.md"><img src="../data/Houston/gt.png" width="260" alt="Houston ground truth"><br>Houston 2013</a></td>
<td align="center"><a href="../data/Trento/Class_details.md"><img src="../data/Trento/gt.png" width="260" alt="Trento ground truth"><br>Trento</a></td>
<td align="center"><a href="../data/WHU-Hi-LongKou/Class_details.md"><img src="../data/WHU-Hi-LongKou/gt.png" width="260" alt="WHU-Hi-LongKou ground truth"><br>WHU-Hi-LongKou</a></td>
</tr>
<tr>
<td align="center"><a href="../data/WHU-Hi-HanChuan/Class_details.md"><img src="../data/WHU-Hi-HanChuan/gt.png" width="260" alt="WHU-Hi-HanChuan ground truth"><br>WHU-Hi-HanChuan</a></td>
<td align="center"><a href="../data/WHU-Hi-HongHu/Class_details.md"><img src="../data/WHU-Hi-HongHu/gt.png" width="260" alt="WHU-Hi-HongHu ground truth"><br>WHU-Hi-HongHu</a></td>
<td align="center"><a href="../data/Chikusei/Class_details.md"><img src="../data/Chikusei/gt.png" width="260" alt="Chikusei ground truth"><br>Chikusei</a></td>
</tr>
<tr>
<td align="center"><a href="../data/HyRANK/Class_details.md"><img src="../data/HyRANK/gt.png" width="260" alt="HyRANK ground truth"><br>HyRANK</a></td>
<td align="center"><a href="../data/MUUFL_Gulfport/Class_details.md"><img src="../data/MUUFL_Gulfport/gt.png" width="260" alt="MUUFL Gulfport ground truth"><br>MUUFL Gulfport</a></td>
<td align="center"><a href="../data/Xiongan/Class_details.md"><img src="../data/Xiongan/gt.png" width="260" alt="Xiongan ground truth"><br>Xiongan</a></td>
</tr>
</table>

## Verification and maintenance

The preview assets are generated from local GT files by [scripts/generate_previews.py](../scripts/generate_previews.py). The script reads label rasters only, never copies hyperspectral cubes, and uses nearest-neighbor resizing for display.

Please report metadata or citation corrections with a primary data page, DOI, paper, or package header as evidence.

## License

[LICENSE](../LICENSE) applies only to content authored in this repository. Every dataset remains subject to its original copyright, license, access conditions, and citation requirements; consult [Sources and usage terms](SOURCES.md) before downloading or using data.
