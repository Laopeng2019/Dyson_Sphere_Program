Dyson Sphere Program's assembly line production trim calculator
----



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
