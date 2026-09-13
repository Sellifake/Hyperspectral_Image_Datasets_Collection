# Data provenance, citations, and usage terms

[中文](../SOURCES.md)

This page records verifiable sources, publications, and package facts. Dataset names, sensors, dimensions, bands, classes, and sample counts are taken from primary data pages, original papers, or inspected files. An entry without an active original download page is explicitly identified.

## Source ledger

| Dataset | Primary page or record | Original paper / required citation | Source status |
|---|---|---|---|
| Indian Pines | [Purdue MultiSpec](https://engineering.purdue.edu/~biehl/MultiSpec/hyperspectral.html) · [PURR record](https://doi.org/10.4231/R7RX991C) | The data record supplies acquisition notes, field notes, and photographs | Official data page |
| Pavia University | [UPV/EHU Hyperspectral Remote Sensing Scenes](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) | The page credits Paolo Gamba, University of Pavia | Original research-group page |
| Pavia Centre | [UPV/EHU Hyperspectral Remote Sensing Scenes](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) | The page credits Paolo Gamba, University of Pavia | Original research-group page |
| Salinas | [UPV/EHU Hyperspectral Remote Sensing Scenes](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) | [NASA/JPL AVIRIS 1998 low-altitude flight index](https://aviris.jpl.nasa.gov/ql/listla98.html) | Original research-group page |
| Kennedy Space Center | [UPV/EHU Hyperspectral Remote Sensing Scenes](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) | The page records the 23 March 1996 AVIRIS acquisition | Original research-group page |
| Botswana | [UPV/EHU Hyperspectral Remote Sensing Scenes](https://www.ehu.eus/ccwintco/index.php/Hyperspectral_Remote_Sensing_Scenes) | The page records the 31 May 2001 EO-1 Hyperion acquisition | Original research-group page |
| Houston 2013 | [IEEE GRSS Data Fusion Contest](https://www.grss-ieee.org/community/technical-committees/2013-ieee-grss-data-fusion-contest/) | [Debes et al., 2014](https://doi.org/10.1109/JSTARS.2014.2305441) | Official contest page |
| Trento | [RSLab, University of Trento](https://rslab.disi.unitn.it/) · [current community mirror](https://github.com/tyust-dayu/Trento) | [Ghamisi, Höfle, and Zhu, 2017](https://doi.org/10.1109/JSTARS.2016.2634863) | Paper verified; no active original download page located |
| WHU-Hi-LongKou | [Wuhan University RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) | [Zhong et al., 2020](https://doi.org/10.1016/j.rse.2020.112012) | Official data page |
| WHU-Hi-HanChuan | [Wuhan University RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) | [Zhong et al., 2020](https://doi.org/10.1016/j.rse.2020.112012) | Official data page |
| WHU-Hi-HongHu | [Wuhan University RSIDEA](https://rsidea.whu.edu.cn/e-resource_WHUHi_sharing.htm) | [Zhong et al., 2020](https://doi.org/10.1016/j.rse.2020.112012) | Official data page |
| Chikusei | [Naoto Yokoya — Download](https://naotoyokoya.com/Download.html) | N. Yokoya and A. Iwasaki, “Airborne hyperspectral data over Chikusei,” SAL-2016-05-27, 2016 | Author data page |
| HyRANK | [HyRANK Hyperspectral Satellite Dataset I](https://doi.org/10.5281/zenodo.1222202) | K. Karantzalos, C. Karakizi, Z. Kandylakis, and G. Antoniou, 2018 · [ISPRS project report](https://www.isprs.org/society/si/SI-2017/ISPRS-SI2017-TC3_WG4_Karantzalos_Report.pdf) | Original data record |
| MUUFL Gulfport | [GatorSense / University of Florida](https://github.com/GatorSense/MUUFLGulfport) | [P. Gader et al., “MUUFL Gulfport Hyperspectral and LiDAR Airborne Data Set,” REP-2013-570, 2013](https://github.com/GatorSense/MUUFLGulfport/blob/master/MUUFLGulfportDataCollection/MUUFLGulfportTechReport.pdf) · [scene-label report](https://ufdc.ufl.edu/IR00009711/00001) | Original project repository |
| Xiongan (Matiwan Village) | [Global Change Research Data Publishing & Repository](https://doi.org/10.3974/geodb.2021.01.02.V1) | [Cen et al., 2020](https://doi.org/10.11834/jrs.20209065) | Official data record |

## Usage terms

The repository license covers only the catalog text, scripts, and preview assets authored for this repository. It does not change a dataset's copyright, license, or citation requirements. Public download access does not by itself grant third-party redistribution rights.

Conditions stated by the linked sources include:

- Chikusei: the author page specifies [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) and requires the stated acknowledgment and technical-report citation.
- WHU-Hi: the Wuhan University RSIDEA page permits academic use only, prohibits commercial use, and requires the specified paper citation.
- Houston 2013: the IEEE GRSS page directs users to request the data by email and acknowledge its terms and conditions.
- MUUFL Gulfport: the project page requires citation of REP-2013-570 when using the data and the 2017 report when using the scene labels.
- Other entries: when the primary page does not state a redistribution license, this catalog does not infer one. Consult the current source terms before mirroring or republishing files.

The storage links in this repository are regional access mirrors only. For datasets with an application, questionnaire, or use restriction, obtain the files from the primary source. A mirror URL is not evidence of permission.

## Inspected-package notes

Spatial dimensions are reported as rows × columns. Label counts are computed pixel by pixel with background 0 excluded. MUUFL uses -1 for unlabeled pixels; those pixels are also excluded.

- **Indian Pines:** the Purdue record and local Indian_pines.mat cube contain 220 bands; the common corrected cube contains 200. This catalog does not repeat the unsupported “224 raw bands” value found on some secondary pages.
- **Pavia Centre / University:** catalog dimensions are the distributed valid matrices, 1096 × 715 and 610 × 340, rather than the source scenes before no-information regions were discarded.
- **Houston 2013:** the name refers to the 2013 contest; the official page dates LiDAR acquisition to 22 June 2012 and HSI acquisition to 23 June 2012.
- **MUUFL Gulfport:** the inspected file is the 1 m, 325 × 220 Campus 1 variant with 64 retained bands. Its metadata records the original 0.5 m image and removal of bands 1–4 and 69–72.
- **HyRANK:** the package contains Dioni, Loukia, Erato, Kirki, and Nefeli. Public GT accompanies Dioni and Loukia only, with 33,527 labeled pixels combined.
- **Xiongan:** the official record states 250 effective bands and 19 land-cover types; Hyperspectral_XiongAn.hdr declares 256 raw bands. The package also contains Groundtruth.img with 19 non-background labels and Farm_roi.img with 20. Both observations are retained rather than collapsed into one value.
- **Trento:** the catalog's authoritative source is a peer-reviewed paper. The available download link is a community mirror and is not labeled as an original source.

## Class statistics and previews

Each class page preserves source label names and lists exact per-class pixel counts:

- [Indian Pines](../data/Indian_Pines/Class_details.md)
- [Pavia University](../data/Pavia/Class_details.md)
- [Pavia Centre](../data/Pavia_Centre/Class_details.md)
- [Salinas](../data/Salinas/Class_details.md)
- [Kennedy Space Center](../data/KSC/Class_details.md)
- [Botswana](../data/Botswana/Class_details.md)
- [Houston 2013](../data/Houston/Class_details.md)
- [Trento](../data/Trento/Class_details.md)
- [WHU-Hi-LongKou](../data/WHU-Hi-LongKou/Class_details.md)
- [WHU-Hi-HanChuan](../data/WHU-Hi-HanChuan/Class_details.md)
- [WHU-Hi-HongHu](../data/WHU-Hi-HongHu/Class_details.md)
- [Chikusei](../data/Chikusei/Class_details.md)
- [HyRANK](../data/HyRANK/Class_details.md)
- [MUUFL Gulfport](../data/MUUFL_Gulfport/Class_details.md)
- [Xiongan](../data/Xiongan/Class_details.md)
