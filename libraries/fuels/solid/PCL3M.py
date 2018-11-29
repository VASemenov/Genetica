#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(0.328626
    -0.772669*scaled_p)
    y_1_2=tanh(1.63302
    +1.28175*scaled_p)
    y_1_3=tanh(-1.26427
    -0.805936*scaled_p)
    scaled_T=(-1.09754
    -0.69965*y_1_1
    +1.33251*y_1_2
    -0.388488*y_1_3)
    scaled_I=(-1.48014
    -0.518548*y_1_1
    +1.00816*y_1_2
    -1.18692*y_1_3)
    (T,I) = (3131+29.9733*scaled_T,295.167+10.8151*scaled_I)
    
    return T, I 
