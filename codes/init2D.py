## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
#♥valeur initilale possible pour le cas 2D
def i1(x,y):
    res=sin(2*pi*x)*sin(2*y*pi)
    return res
def iexact1(x,y,t,cx,cy):
    res=sin(2*pi*(x-cx*t))*sin(2*pi*(y-cy*t))
    return res