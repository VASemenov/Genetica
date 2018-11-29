#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-1.08947
    -1.40624*scaled_p)
    y_1_2=tanh(0.387092
    -0.670785*scaled_p)
    y_1_3=tanh(-0.144553
    -0.102577*scaled_p)
    scaled_T=(-0.180132
    -0.965068*y_1_1
    -0.952468*y_1_2
    +0.337228*y_1_3)
    scaled_I=(-0.50267
    -1.15393*y_1_1
    -0.568905*y_1_2
    -0.374627*y_1_3)
    (T,I) = (2606.67+25.0173*scaled_T,212.167+7.19491*scaled_I)
    
    return T, I 
