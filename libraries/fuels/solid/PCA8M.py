#!/usr/bin/python

from math import tanh

def expression (p) : 

    scaled_p=(p-11.3333)/5.71548
    y_1_1=tanh(1.2419
    +1.41288*scaled_p)
    y_1_2=tanh(-0.595295
    +0.18322*scaled_p)
    y_1_3=tanh(0.475267
    -0.37518*scaled_p)
    scaled_T=(0.286623
    +1.06761*y_1_1
    +0.841899*y_1_2
    -1.0914*y_1_3)
    scaled_I=(-0.0382256
    +1.21543*y_1_1
    +0.681451*y_1_2
    -0.737305*y_1_3)
    (T,I) = (3456.5+42.1082*scaled_T,346.833+13.6002*scaled_I)
    
    return T, I 
