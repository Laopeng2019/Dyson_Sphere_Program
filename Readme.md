戴森球计划的流水线生产配平计算器 / Dyson Sphere Program's assembly line production trim calculator
====

Please see [here](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md) for the introduction in English.

目录
> [简介](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme.md#%E7%AE%80%E4%BB%8B)<br>
> [使用步骤](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme.md#%E4%BD%BF%E7%94%A8%E6%AD%A5%E9%AA%A4)<br>
> [计算结果](https://github.com/Laopeng2019/Dyson_Sphere_Program#%E8%AE%A1%E7%AE%97%E7%BB%93%E6%9E%9C)<br>


## 简介

相比于其他计算器，除了提供了普通的配平功能，这个计算器实现了计算极限生产线长度（比如一条普通速度的传送带可以最多放几个铁块冶炼炉），以及如何最低分拣器的等级（最近的生产设施可以使用的最低分拣器等级）。

总的来说，就是为密集型生产提供数字计算。

编程语言是 `Python`，使用了 `pandas` 框架读取生产公式数据以及配置（包括速度和输入）。

通过运行 `rate_calculation.py` 文件可以读取输入文件，得到结果文件，可以在Excel里面打开查看。


## 使用步骤

### 输入配平计算与需求配置速度

`config.xlsx` 文件是储存输入配平计算与需求配置速度的文件。

- 生产类型 / Production type : 

- 速度（倍率） /  Speed (ratio)	

- 生产物品 / Production ：输入需要配平计算的物品。

- 生产数量 / Production quantity ：输入需要计算的数量（个 / 每分钟）。

| 生产物品 / Production | 生产数量 / Production quantity |
| :---: | :---: |
| 白糖 | 1200 |



### 生产公式
`data.xlsx` 文件是储存生产公式的文件，做成Excel文件方便输入和更改。

不同的是在公式里，氢之类的副产物会变成带负号的原材料，以方便计算。

比如: 

```
1精炼油 + 1氢 = 2原油 -> 1精炼油 = 2原油 - 1氢
```


## 计算结果
`result.xlsx` 文件是储存计算结果的文件。其中包括：

- 生产物品 / Production	
- 倍数 / times	
- 生产类型 / Production type	
- 预计速度(个每分钟) / Estimated speed(one per minute)	
- 需要速度(个每分钟) / Demanded speed(one per minute)	
- 最小分拣速度等级 / Minimum sorting speed level	
- 传送速度等级 / Transmission speed level	
- 最适传送长度 / Optimal transmission length

倍数是指需要多少个设施来生产，生产类型指需要哪里设施

其中预计速度是游戏里生产时候标定的速度，由生产公式计算得出。

需要速度是根据上级产物需要的生产速度，除以当前原料产量，得出的当前的需要速度。

