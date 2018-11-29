#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.831569
    +1.24072*scaled_p)
    y_1_2=tanh(-1.66054
    +1.42652*scaled_p)
    y_1_3=tanh(0.405205
    -0.224892*scaled_p)
    scaled_T=(1.01543
    -0.067928*y_1_1
    +1.02845*y_1_2
    +0.135751*y_1_3)
    scaled_I=(-0.10553
    +1.0645*y_1_1
    +0.451164*y_1_2
    +0.124201*y_1_3)
    (T,I) = (2302+14.6287*scaled_T,287.5+10.7098*scaled_I)
    
    return T, I 
