#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.459232
    +0.856272*scaled_p)
    y_1_2=tanh(-0.443426
    +0.446704*scaled_p)
    y_1_3=tanh(-0.513465
    -0.512644*scaled_p)
    scaled_T=(-0.191872
    +0.614127*y_1_1
    +0.704102*y_1_2
    -0.841348*y_1_3)
    scaled_I=(-0.157102
    +0.923173*y_1_1
    +0.462948*y_1_2
    -0.407452*y_1_3)
    (T,I) = (3164.33+144.265*scaled_T,197+8.5557*scaled_I)
    
    return T, I 
