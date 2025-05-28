# Hyperspectral_Image_Datasets_Collection

## 选择语言

- [中文](#中文)
- [English](en/README.md)

## 中文

### 介绍

本仓库包含本人在研究生期间常用的高光谱图像数据集，数据集也可以在夸克网盘上获取。

### 下载链接

- **夸克网盘**: [全部数据连接](https://pan.baidu.com/s/16hqvgJrxAgLm9_0o1Ljbwg?pwd=vstw)

### 数据集

#### 1. 印度松树（Indian Pines）数据集

- **数据采集时间**: 1992年
- **原始链接**: [Indian Pines Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Indian_Pines)
- **描述**: 印度松树数据集是一个常用于高光谱图像处理的基准数据集，包含来自印第安纳州普渡大学实验农场的224个波段的高光谱图像。
- **像素大小**: 145 x 145
- **波段数**: 224(原始)/200(去除吸水波段)
- **类别总数**：[16](data/Indian_Pines/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Indian_Pines/gt.png)

---

#### 2. 帕维亚大学（Pavia University）数据集

- **数据采集时间**: 2001年
- **原始链接**: [Pavia University Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Pavia_Centre_and_University)
- **描述**: ROSIS传感器在意大利北部帕维亚上空飞行时拍摄的大学校园场景。
- **像素大小**: 610 x 610(大学)/610 x 340(去除黑色像素)
- **波段数**: 103
- **类别总数**：[9](data/Pavia/Class_details.md)
- **GT(标签) 图像**
  ![Pavia University Ground Truth](data/Pavia/gt.png)

---

#### 3. 帕维亚中心（Pavia Centre）数据集

- **数据采集时间**: 未知
- **原始链接**: [Pavia Centre Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Pavia_Centre_and_University)
- **描述**: ROSIS传感器在意大利北部帕维亚上空飞行时拍摄的城市场景中心部分。
- **像素大小**: 1096 x 1096
- **波段数**: 102
- **类别总数**：[9](data/Pavia_Centre/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Pavia_Centre/gt.png)

---

#### 4. 萨利纳斯（Salinas）数据集

- **数据采集时间**: 未知
- **原始链接**: [Salinas Dataset](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Salinas_scene)
- **描述**: 萨利纳斯数据集是一个高光谱图像处理的基准数据集，包含来自美国加利福尼亚州萨利纳斯谷的224个波段的高光谱图像。
- **像素大小**: 512 x 217
- **波段数**: 224(全部)/204(去除吸水波段)
- **类别总数**：[16](data/Salinas/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Salinas/gt.png)

---

#### 5. 肯尼迪航天中心（KSC）数据集

- **数据采集时间**: 1996年3月23日
- **原始链接**: [KSC Dataset](https://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Kennedy_Space_Center_.28KSC.29)
- **描述**: NASA 的 AVIRIS 仪器于1996年3月23日在佛罗里达州的肯尼迪航天中心（KSC）上空获取数据，原始224个波段，去除水吸收和低信噪比波段后使用176个波段。
- **像素大小**: 512 x 614
- **波段数**: 224(原始)/176(去除)
- **类别总数**：[13](data/KSC/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/KSC/gt.png)

---

#### 6. 博茨瓦纳（Botswana）数据集

- **数据采集时间**: 2001-2004年
- **原始链接**: [Botswana Dataset](https://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Botswana)
- **描述**: NASA 的 EO-1 卫星 Hyperion 传感器在博茨瓦纳三角洲获取数据，原始242个波段，去除水吸收和低信噪比波段后使用145个波段。
- **像素大小**: 1476 x 256
- **波段数**: 242(原始)/145(去除)
- **类别总数**：[14](data/Botswana/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Botswana/gt.png)

---

#### 7. 休斯顿（Houston）数据集

- **数据采集时间**: 2013年
- **原始链接**: [Houston Dataset](https://hyperspectral.ee.uh.edu/?page_id=459)
- **描述**: IEEE GRSS 数据融合竞赛使用的休斯顿高光谱图像，包含城市区域和标签，144个波段。
- **像素大小**: 349 x 1905
- **波段数**: 144
- **类别总数**：[15](data/Houston/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Houston/gt.png)

---

#### 8. 特伦托（Trento）数据集

- **数据采集时间**: 未知
- **原始链接**: [Trento Dataset](https://github.com/tyust-dayu/Trento)
- **描述**: 多源数据集包含意大利特伦托地区的高光谱图像（63波段）和 LiDAR 数据，空间分辨率1米。
- **像素大小**: 166 x 600
- **波段数**: 63
- **类别总数**：[6](data/Trento/Class_details.md)
- **GT(标签) 图像**
  ![Ground Truth Image](data/Trento/gt.png)

---

#### 9. WHU-Hi-LongKou 数据集
- **数据采集时间**: 2018年7月17日  
- **原始数据（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-LongKou/WHU_Hi_LongKou.mat  
- **GT 标签（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-LongKou/WHU_Hi_LongKou_gt.mat  
- **描述**: 使用 Headwall Nano-Hyperspec 传感器搭载 DJI M600 Pro 无人机在 500 m 高度获取，覆盖湖北省龙口市农业区，共270个波段，空间分辨率约0.463 m 
- **像素大小**: 550 x 400 
- **波段数**: 270 
- **类别总数**: [9](data/WHU-Hi-LongKou/Class_details.md)  
- **GT(标签) 图像**  
  ![Ground Truth Image](data/WHU-Hi-LongKou/gt.png)

#### 10. WHU-Hi-HanChuan 数据集
- **数据采集时间**: 2016年6月17日 17:57–18:46  
- **原始数据（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-HanChuan/WHU_Hi_HanChuan.mat  
- **GT 标签（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-HanChuan/WHU_Hi_HanChuan_gt.mat  
- **描述**: 使用 Headwall Nano-Hyperspec 传感器搭载 Leica Aibot X6 无人机在 250 m 高度采集，研究区为湖北省汉川市城乡结合部，多种作物与建筑覆盖区，共274个波段，空间分辨率约0.109 m
- **像素大小**: 1217 x 303
- **波段数**: 274
- **类别总数**: [13](data/WHU-Hi-HanChuan/Class_details.md)  
- **GT(标签) 图像**  
  ![Ground Truth Image](data/WHU-Hi-HanChuan/gt.png)

#### 11. WHU-Hi-HongHu 数据集
- **数据采集时间**: 2017年11月20日 16:23–17:37  
- **原始数据（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-HongHu/WHU_Hi_HongHu.mat  
- **GT 标签（.mat）**: http://rsidea.whu.edu.cn/code_data/WHU-Hi/Matlab_data_format/WHU-Hi-HongHu/WHU_Hi_HongHu_gt.mat  
- **描述**: 使用 Headwall Nano-Hyperspec 传感器搭载 DJI M600 Pro 无人机在 100 m 高度获取，研究区为湖北省洪湖市农业—园区交界地带，共270个波段，空间分辨率约0.043 
- **像素大小**: 940 x 475
- **波段数**: 270 
- **类别总数**: [22](data/WHU-Hi-HongHu/Class_details.md)  
- **GT(标签) 图像**  
  ![Ground Truth Image](data/WHU-Hi-HongHu/gt.png)