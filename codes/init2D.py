## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
#♥valeur initilale possible pour le cas 2D
def i1(x,y):
    res=sin(3*pi*x)*sin(3*y*pi)
    return res
def iexact1(x,y,t,cx,cy):
    res=sin(3*pi*(x-cx*t))*sin(3*pi*(y-cy*t))
    return res
    
    
def i2(x,y):
    res=exp(-3*(x+y)**2)
    return res