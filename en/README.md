# Hyperspectral Image Datasets Collection

### Introduction
This repository contains commonly used hyperspectral image datasets for research purposes. The datasets are also available on Baidu Netdisk and Quark Netdisk.

### Download Links
- **Baidu Netdisk**: [(https://pan.baidu.com/s/13Bd_8vZT9pIfqbTxNYlyEw?pwd=v81w)]

### Datasets
#### 1. Indian Pines (IP) Dataset
- **Data Collection Time**: 1992
- **Original Link**: [Indian Pines Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Indian_Pines)
- **Description**: The Indian Pines dataset is a commonly used benchmark in hyperspectral image processing, containing 224-band hyperspectral images from Purdue University's agricultural site in Indiana. It is used to test the performance of classification algorithms.
- **Pixel Size**: 145 x 145
- **Number of Bands**: 224(origional)/200 (corrected:After removing the bands covering the region of water absorption)
- **Class number**：16 [Details](../data/Indian_Pines/Class_details.md)
- **GT(label) image**
![Ground Truth Image](../data/Indian_Pines/300px-Indian_pines_gt.png)

#### 2. Pavia University (PU) Dataset
- **Data Collection Time**: 2001
- **Original Link**: [Pavia University Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Pavia_Centre_and_University)
- **Description**: These are two scenes acquired by the ROSIS sensor during a flight campaign over Pavia, nothern Italy》
- **Pixel Size**: 610 x 610(University)/610 x 340(Exclude backgroungd pixel)
- **Number of Bands**: 103
- **Class number**：9 [Details](data/Pavia/Class_details.md)
- **GT igame**:
![Pavia University Ground Truth](data/Pavia/300px-PaviaU_gt.png)

#### 3. Houston University (HU) Dataset
- **Data Collection Time**: 2013
- **Original Link**: [Houston University Dataset](https://hyperspectral.ee.uh.edu/?page_id=459)
- **Description**: The Houston University dataset was used in the IEEE GRSS Data Fusion Contest, containing hyperspectral images and corresponding ground truth labels from the urban area of Houston, Texas, for evaluating classification algorithms.
- **Pixel Size**: 349 x 1905
- **Number of Bands**: 144
- **GT image**:(![url_to_gt_image](https://production-media.paperswithcode.com/datasets/Screen_Shot_2021-01-27_at_9.46.45_PM.png))


