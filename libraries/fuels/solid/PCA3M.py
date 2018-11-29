#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-0.793134
    +1.33958*scaled_p)
    y_1_2=tanh(-1.2587
    -1.30325*scaled_p)
    y_1_3=tanh(1.19629
    +2.91575*scaled_p)
    scaled_T=(-0.744453
    +0.464309*y_1_1
    -1.69656*y_1_2
    -0.207818*y_1_3)
    scaled_I=(-0.295739
    +1.82097*y_1_1
    -1.71037*y_1_2
    -1.82959*y_1_3)
    (T,I) = (3185.83+27.5493*scaled_T,284+12.506*scaled_I)
    
    return T, I 
