#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.663355
    +0.878321*scaled_p)
    y_1_2=tanh(0.471228
    -0.504095*scaled_p)
    y_1_3=tanh(-0.228261
    +0.115277*scaled_p)
    scaled_T=(-0.118918
    +1.15072*y_1_1
    -0.686457*y_1_2
    +0.0546296*y_1_3)
    scaled_I=(-0.219006
    +1.20842*y_1_1
    -0.657965*y_1_2
    -0.268547*y_1_3)
    (T,I) = (3974.83+85.3684*scaled_T,285.833+11.479*scaled_I)
    
    return T, I 
