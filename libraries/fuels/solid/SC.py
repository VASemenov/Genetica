#!/usr/bin/python

from math import tanh

FORMULA = {
    'C': 22.324,
    'H': 30.105,
    'O': 34.686,
    'N': 10.461,
    'Al': 0,
    'Na': 0,
    'Mg': 0,
    'S': 0,
    'Cl': 0,
    'K': 0,
    'B': 0,
    'F': 0
}

B = 185

def expression (p) : 

    scaled_p=(p-10)/4.74342
    y_1_1=tanh(0.694558
    -0.00665811*scaled_p)
    y_1_2=tanh(0.0984529
    -0.472018*scaled_p)
    y_1_3=tanh(-0.739706
    -1.48408*scaled_p)
    scaled_T=(-0.37553
    -0.196656*y_1_1
    -0.0957034*y_1_2
    -1.23367*y_1_3)
    scaled_I=(-0.126057
    -0.36165*y_1_1
    -0.588912*y_1_2
    -0.968554*y_1_3)
    (T,I) = (2558.17+2.80916*scaled_T,278.508+5.62843*scaled_I)
    
    return T, I 
