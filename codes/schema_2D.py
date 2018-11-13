#CARLIER Tiffanie
#-*- coding: utf-8 -*-
#module des differents schema possible pour la resolution de l'equation de transport 2D
from pylab import *

#ici dx pas d'espace en x et dy pas d'espace en y
#on etudie le domaine sur (0,1)*(0,1)
def s1(cx,cy,f,x,y,t,u,uN,dt,dx,dy): #schema stable car tient compte du signe de c
    if cx>0 and cy>0:
        for i in arange(0,len(x)):
            uN[i,0]=f(x[i],0) #creer un fichier pour des valeurs de conditions aux bords cas 2D nomme init
        for j in arange(0,len(y)):
            uN[0,j]=f(0,y[j]) #creer un fichier pour des valeurs de conditions aux bords cas 2D nomme init
        uN[[i,j]]=u[[i,j]]+cx*(dt/dx)*(u[:-1,1:]-u[1:,1:])+cy*(dt/dy)*(u[1:,:-1]-u[1:,1:])
    if cx<0 and cy<0:
        for i in arange(0,len(x)):
            uN[i,-1]=f(x[i],1)
        for j in arange(0,len(y)):
            uN[-1,j]=f(1,y[j])
        uN[:-1,:-1]=u[:-1,:-1]+cx*(dt/dx)*(u[:-1,:-1]-u[1:,:-1])+cy*(dt/dy)*(u[:-1,:-1]-u[:-1,1:])
        
    if cx<0 and cy>0:
        for i in arange(0,len(x)):
            uN[i,0]=f(x[i],0)
        for j in arange(0,len(y)):
            uN[-1,j]=f(1,y[j])
        uN[:-1,:-1]=u[:-1,:-1]+cx*(dt/dx)*(u[:-1,:-1]-u[1:,:-1])+cy*(dt/dy)*(u[1:,:-1]-u[1:,1:])

        
    if cx>0 and cy<0:
        for i in arange(0,len(x)):
            uN[i,-1]=f(x[i],1)
        for j in arange(0,len(y)):
            uN[0,j]=f(0,y[j])
        uN[:-1,:-1]=u[:-1,:-1]+cx*(dt/dx)*(u[:-1,1:]-u[1:,1:])+cy*(dt/dy)*(u[:-1,:-1]-u[:-1,1:])
    return uN
    
#message d'erreur too many array