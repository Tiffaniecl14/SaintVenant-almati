#Tiffanie CARLIER
#-*- coding: utf-8 -*-
from pylab import *

#une condition initiale possible pour le probleme de transport
#la bibliotheque pylab permet d'eviter l'utilisation des abreviations numpy

def i1(x):
    y=cos(2*pi*x)
    return y

def i2(x):
    y=-(2/pi)*arctan(100*(x-0.5))
    return y
    
def i3(x):
    return 1.*(x<0.2)
    

