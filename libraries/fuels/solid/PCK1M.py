#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-0.510609
    +0.486915*scaled_p)
    y_1_2=tanh(0.638243
    -0.488281*scaled_p)
    y_1_3=tanh(1.65754
    +1.20741*scaled_p)
    scaled_T=(-0.460534
    +0.433564*y_1_1
    -1.17742*y_1_2
    +1.68757*y_1_3)
    scaled_I=(-0.789481
    +0.526876*y_1_1
    -0.787475*y_1_2
    +1.89822*y_1_3)
    (T,I) = (3518.83+50.0057*scaled_T,250.333+9.66782*scaled_I)
    
    return T, I 
