#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.411003
    -0.629553*scaled_p)
    y_1_2=tanh(-1.40662
    -1.24912*scaled_p)
    y_1_3=tanh(0.399317
    -0.0133633*scaled_p)
    scaled_T=(-0.776245
    -0.772818*y_1_1
    -1.42998*y_1_2
    +0.211239*y_1_3)
    scaled_I=(-0.854376
    -0.581748*y_1_1
    -1.55768*y_1_2
    +0.00831002*y_1_3)
    (T,I) = (2906.17+30.6752*scaled_T,254.833+7.85918*scaled_I)
    
    return T, I 
