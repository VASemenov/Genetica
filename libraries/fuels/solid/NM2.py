#!/usr/bin/python

from math import tanh

FORMULA = {
    'C': 23.027,
    'H': 29.974,
    'O': 33.974,
    'N': 9.837,
    'Al': 0,
    'Na': 0,
    'Mg': 0.496,
    'S': 0,
    'Cl': 0,
    'K': 0,
    'B': 0,
    'F': 0
}

B = 177

def expression (p) : 

    scaled_p=(p-10)/4.74342
    y_1_1=tanh(-0.300353
    -0.58362*scaled_p)
    y_1_2=tanh(-0.568824
    +0.642252*scaled_p)
    y_1_3=tanh(-1.67798
    -1.56445*scaled_p)
    scaled_T=(-0.574864
    -0.337045*y_1_1
    +0.579852*y_1_2
    -1.1402*y_1_3)
    scaled_I=(-0.474458
    -0.785721*y_1_1
    +0.518355*y_1_2
    -0.782257*y_1_3)
    (T,I) = (2345.12+1.18257*scaled_T,268.906+5.90084*scaled_I)
    
    return T, I 
