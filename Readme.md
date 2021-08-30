戴森球计划的流水线生产配平计算器/Dyson Sphere Program's assembly line production trim calculator
====

[Please see the bottom for the introduction in English.]()

> [简介]()<br>
> [实现步骤]()<br>
> [实现结果]()<br>


## 简介

相比于其他计算器，这个计算器实现了计算极限生产线长度（比如一条普通速度的传送带可以最多放几个铁块冶炼炉），以及如何最低分拣器的等级。

总的来说，就是为密集型生产提供数字计算。

编程语言是 `Python`，使用了 `pandas` 框架读取生产公式数据以及配置（包括速度和输入）。




## 输入配平计算与需求配置速度
`config.xlsx` 文件是储存输入配平计算与需求配置速度的文件。

生产物品 / Production ：输入需要配平计算的物品。

生产数量 / Production quantity ：输入需要计算的数量（个 / 每分钟）。

| 生产物品 / Production | 生产数量 / Production quantity |
| :---: | :---: |
| 白糖 | 1200 |



## 生产公式
`data.xlsx` 文件是储存生产公式的文件，做成Excel文件方便输入和更改。

不同的是在公式里，氢之类的副产物会变成带负号的原材料，以方便计算。

```
比如 
1精炼油 + 1氢 = 2原油 -> 1精炼油 = 2原油 - 1氢
```


## 计算结果
`result.xlsx` 文件是储存计算结果的文件

其中预计速度是游戏里生产时候标定的速度，由生产公式计算得出。

需要速度是根据上级产物需要的生产速度，除以当前原料产量，得出的当前的需要速度。




## Introduction
Compared with other calculators, this calculator realizes the calculation of the limit production line length (for example, a normal speed conveyor belt can put at most several iron smelting furnaces), and how to minimize the level of the sorter.

In general, it is to provide digital calculations for intensive production.

The programming language is Python, and the pandas framework is used to read the production formula data and configuration (including speed and input).

This program uses a recursive structure.

---

## Input trim calculation and demand configuration speed
The file **config.xlsx** stores the input balance calculation and the demanded configuration speed.
Production is the item that needs to be balanced and calculated, and production quantity is the quantity of production that needs to be calculated (one/per minute).


---

## Production formula
A file **data.xlsx** stores production formulas and is made into an Excel file for easy input and modification.
The difference is that in the formula, by-products such as hydrogen will become raw materials with a negative sign to facilitate calculations.
For example,
>1 Refined oil + 1 Hydrogen = 2 Crude oil -> 1 Refined oil = 2 Crude oil - 1 Hydrogen

---

## Calculation results
The file **result.xlsx** stores the calculation results.
The estimated speed is the calibrated speed during production in the game, which is calculated by the production formula.
The demanded speed is the current demanded speed based on the production speed required by the superior product, divided by the current raw material output.
The demanded speed can also be a given value, such as
>White matrix，1200
