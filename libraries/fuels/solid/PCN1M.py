#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.307496
    -0.220764*scaled_p)
    y_1_2=tanh(-0.133568
    +0.792824*scaled_p)
    y_1_3=tanh(-1.02253
    -1.22568*scaled_p)
    scaled_T=(-0.274409
    -0.253899*y_1_1
    +0.951273*y_1_2
    -0.751562*y_1_3)
    scaled_I=(-0.274894
    -0.823499*y_1_1
    +0.448343*y_1_2
    -1.06638*y_1_3)
    (T,I) = (3953.33+85.3549*scaled_T,308.167+11.8561*scaled_I)
    
    return T, I 
