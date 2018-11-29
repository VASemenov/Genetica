#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-1.7681
    -1.53558*scaled_p)
    y_1_2=tanh(0.104455
    -0.124195*scaled_p)
    y_1_3=tanh(0.184492
    -0.764611*scaled_p)
    scaled_T=(-0.628542
    -1.08898*y_1_1
    +0.0528299*y_1_2
    -0.942279*y_1_3)
    scaled_I=(-0.654312
    -1.11585*y_1_1
    +0.104366*y_1_2
    -0.93136*y_1_3)
    (T,I) = (3689.17+64.2975*scaled_T,321.167+13.0754*scaled_I)
    
    return T, I 
