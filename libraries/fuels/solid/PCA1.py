#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-2.00769
    -1.75003*scaled_p)
    y_1_2=tanh(0.305443
    -0.823877*scaled_p)
    y_1_3=tanh(1.30351
    +0.989304*scaled_p)
    scaled_T=(-0.685335
    -1.26938*y_1_1
    -0.798077*y_1_2
    -0.0556093*y_1_3)
    scaled_I=(-0.958334
    -0.624684*y_1_1
    -0.666949*y_1_2
    +0.953104*y_1_3)
    (T,I) = (2787.5+12.145*scaled_T,262+7.18331*scaled_I)
    
    return T, I 
