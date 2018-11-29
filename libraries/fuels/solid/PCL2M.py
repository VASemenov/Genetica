#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-1.33367
    -1.38574*scaled_p)
    y_1_2=tanh(0.256756
    -0.399199*scaled_p)
    y_1_3=tanh(0.74874
    -0.456912*scaled_p)
    scaled_T=(-0.146367
    -1.22529*y_1_1
    -0.294088*y_1_2
    -0.924404*y_1_3)
    scaled_I=(-0.30856
    -1.17568*y_1_1
    -0.80356*y_1_2
    -0.383295*y_1_3)
    (T,I) = (2728+15.1129*scaled_T,275.333+10.4817*scaled_I)
    
    return T, I 
