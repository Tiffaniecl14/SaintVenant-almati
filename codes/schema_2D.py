#CARLIER Tiffanie
#-*- coding: utf-8 -*-
#module des differents schema possible pour la resolution de l'equation de transport 2D
from pylab import *

#ici dx pas d'espace en x et dy pas d'espace en y
#on etudie le domaine sur (0,1)*(0,1)
#ajouter g fonction condition periodique ???
def s1(cx,cy,x,y,t,u,uold,dt,dx,dy): #schema stable car tient compte du signe de c

    if cx>=0 and cy>=0:
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                u[i][j]=uold[i][j]+cx*(dt/dx)*(uold[i-1][j]-uold[i][j])+cy*(dt/dy)*(uold[i][j-1]-uold[i][j])
            
    if cx>=0 and cy<=0:
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                u[i][j]=uold[i][j]+cx*(dt/dx)*(uold[i-1][j]-uold[i][j])+cy*(dt/dy)*(uold[i][j]-uold[i][j+1])
            
    if cx<=0 and cy>=0:
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                u[i][j]=uold[i][j]+cx*(dt/dx)*(uold[i][j]-uold[i+1][j])+cy*(dt/dy)*(uold[i][j-1]-uold[i][j])
            
    if cx<=0 and cy<=0:
        for i in range(1,len(x)-1):
            for j in range(1,len(y)-1):
                u[i][j]=uold[i][j]+cx*(dt/dx)*(uold[i][j]-uold[i+1][j])+cy*(dt/dy)*(uold[i][j]-uold[i][j+1])
                
            
    return u

