#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-0.401296
    +0.450346*scaled_p)
    y_1_2=tanh(0.899403
    -0.411873*scaled_p)
    y_1_3=tanh(0.581374
    +0.889707*scaled_p)
    scaled_T=(0.216195
    +0.763499*y_1_1
    -0.349781*y_1_2
    +0.954258*y_1_3)
    scaled_I=(0.0524381
    +0.692479*y_1_1
    -0.154655*y_1_2
    +1.01703*y_1_3)
    (T,I) = (2530.67+62.6695*scaled_T,299.833+12.8595*scaled_I)
    
    return T, I 
