#!/usr/bin/python

from math import tanh

FORMULA = {
    'C': 23.498,
    'H': 30.259,
    'O': 34.190,
    'N': 10.011,
    'Al': 0,
    'Na': 0,
    'Mg': 0,
    'S': 0,
    'Cl': 0,
    'K': 0,
    'B': 0,
    'F': 0
}

B = 180

def expression (p) : 

    scaled_p=(p-10)/4.74342
    y_1_1=tanh(-0.302944
    -0.582555*scaled_p)
    y_1_2=tanh(-0.569165
    +0.643996*scaled_p)
    y_1_3=tanh(-1.67719
    -1.56266*scaled_p)
    scaled_T=(-0.577769
    -0.33616*y_1_1
    +0.578737*y_1_2
    -1.14228*y_1_3)
    scaled_I=(-0.475978
    -0.78381*y_1_1
    +0.521107*y_1_2
    -0.784321*y_1_3)
    (T,I) = (2345.12+1.18257*scaled_T,268.906+5.90084*scaled_I)
    
    return T, I 
