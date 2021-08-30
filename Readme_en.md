Dyson Sphere Program's assembly line production trim calculator
----


中文请看[这里](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/0f9e5a7e21454b4f58d80308b9254de9a3a2a719/Readme_en.md)。

> [Introduction](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#introduction)<br>
> [How to use](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#how-to-use)<br>
> [Calculation results](https://github.com/Laopeng2019/Dyson_Sphere_Program/blob/master/Readme_en.md#calculation-results)<br>

## Introduction
Compared with other calculators, this calculator realizes the calculation of the limit production line length (for example, a normal speed conveyor belt can put at most several iron smelting furnaces), and how to minimize the level of the sorter.

In general, it is to provide digital calculations for intensive production.

The programming language is Python, and the pandas framework is used to read the production formula data and configuration (including speed and input).

This program uses a recursive structure.


## How to use

### Input trim calculation and demand configuration speed.

The file **config.xlsx** stores the input balance calculation and the demanded configuration speed.

Production is the item that needs to be balanced and calculated, and production quantity is the quantity of production that needs to be calculated (one/per minute).

Such as,
```
| 生产物品 / Production | 生产数量 / Production quantity |
| :---: | :---: |
| White matrix | 1200 |
```

### Production formula

A file **data.xlsx** stores production formulas and is made into an Excel file for easy input and modification.

The difference is that in the formula, by-products such as hydrogen will become raw materials with a negative sign to facilitate calculations.

For example,

```
1 Refined oil + 1 Hydrogen = 2 Crude oil -> 1 Refined oil = 2 Crude oil - 1 Hydrogen
```

## Calculation results

The file **result.xlsx** stores the calculation results.

The estimated speed is the calibrated speed during production in the game, which is calculated by the production formula.

The demanded speed is the current demanded speed based on the production speed required by the superior product, divided by the current raw material output.

