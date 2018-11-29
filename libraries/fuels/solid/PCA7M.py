#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-1.85395
    -1.79556*scaled_p)
    y_1_2=tanh(0.482545
    -1.12778*scaled_p)
    y_1_3=tanh(0.697813
    -0.0086805*scaled_p)
    scaled_T=(-0.533632
    -1.06379*y_1_1
    -0.714035*y_1_2
    +0.0862146*y_1_3)
    scaled_I=(-0.539897
    -1.06626*y_1_1
    -0.711597*y_1_2
    +0.0923277*y_1_3)
    (T,I) = (4138.67+92.472*scaled_T,301.833+12.8595*scaled_I)
    
    return T, I 
