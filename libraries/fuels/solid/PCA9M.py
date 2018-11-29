#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(-0.176991
    +0.533568*scaled_p)
    y_1_2=tanh(1.89024
    +1.93111*scaled_p)
    y_1_3=tanh(-0.789168
    +0.0127819*scaled_p)
    scaled_T=(-0.52527
    -0.0287487*y_1_1
    +1.62102*y_1_2
    +0.786709*y_1_3)
    scaled_I=(-0.19447
    +1.14563*y_1_1
    +0.88318*y_1_2
    +0.256614*y_1_3)
    (T,I) = (2977.83+39.5731*scaled_T,254.5+10.7098*scaled_I)
    
    return T, I 
