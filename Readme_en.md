Dyson Sphere Program's assembly line production trim calculator
====


中文请看[这里](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme.md)。

Contents
> [Introduction](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#introduction)<br>
> [How to use](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#how-to-use)<br>
> [Calculation results](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#calculation-results)<br>

## Introduction
Compared with other calculators, this calculator realizes the calculation of the limit production line length (for example, a normal speed conveyor belt can put at most several iron smelting furnaces), and how to minimize the level of the sorter.

In general, it is to provide digital calculations for intensive production.

The programming language is `Python`, and the `pandas` framework is used to read the production formula data and configuration (including speed and input).

This program uses a recursive structure.

Attention: The production formula has not been written completely. Items not in the formula need to be filled out by hand.


## How to use

### Input trim calculation and demand configuration speed.

The file `config.xlsx` stores the input balance calculation and the demanded configuration speed.

Production is the item that needs to be balanced and calculated, and production quantity is the quantity of production that needs to be calculated (one/per minute).

Such as,

| 生产物品 / Production | 生产数量 / Production quantity |
| :---: | :---: |
| White matrix | 1200 |


### Production formula

A file `data.xlsx` stores production formulas and is made into an Excel file for easy input and modification.


- 生产类型 / Production type :

- 速度（倍率） /  Speed (ratio)	:

- 生产物品 / Production :

- 生产数量 / Production quantity :

What is different is that in the formula, by-products such as hydrogen will become raw materials with a negative sign to facilitate calculations.

For example,

```
1 Refined oil + 1 Hydrogen = 2 Crude oil -> 1 Refined oil = 2 Crude oil - 1 Hydrogen
```

## Calculation results

The file `result.xlsx` stores the calculation results, 
which include:
- 生产物品 / Production	
- 倍数 / times	
- 生产类型 / Production type	
- 预计速度(个每分钟) / Estimated speed(one per minute)	
- 需要速度(个每分钟) / Demanded speed(one per minute)	
- 最小分拣速度等级 / Minimum sorting speed level	
- 传送速度等级 / Transmission speed level	
- 最适传送长度 / Optimal transmission length

The estimated speed is the calibrated speed during production in the game, which is calculated by the production formula.

The demanded speed is the current demanded speed based on the production speed required by the superior product, divided by the current raw material output.

