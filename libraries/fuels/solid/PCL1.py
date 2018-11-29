#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(1.64066
    +1.5391*scaled_p)
    y_1_2=tanh(-0.605769
    +0.922048*scaled_p)
    y_1_3=tanh(-0.381554
    +0.205472*scaled_p)
    scaled_T=(-0.471118
    +1.19027*y_1_1
    +0.728875*y_1_2
    +0.107904*y_1_3)
    scaled_I=(-0.519347
    +1.28234*y_1_1
    +0.580115*y_1_2
    +0.306373*y_1_3)
    (T,I) = (3103.33+45.0185*scaled_T,257.5+9.33274*scaled_I)
    
    return T, I 
