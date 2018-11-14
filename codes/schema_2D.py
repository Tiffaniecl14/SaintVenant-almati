#CARLIER Tiffanie
#-*- coding: utf-8 -*-
#module des differents schema possible pour la resolution de l'equation de transport 2D
from pylab import *

#ici dx pas d'espace en x et dy pas d'espace en y
#on etudie le domaine sur (0,1)*(0,1)
#ajouter g fonction condition periodique ???
def s1(cx,cy,f,g,x,y,t,u,uN,dt,dx,dy): #schema stable car tient compte du signe de c

    if cx>0 and cy>0:
        for i in arange(0,len(x)):
            uN[i,0]=g(x[i],0,t) #creer un fichier pour des valeurs de conditions aux bords cas 2D nomme init
            uN[i,len(y)-1]=uN[i,0]
            
            
        for j in arange(0,len(y)):
            uN[0,j]=g(0,y[j],t) #creer un fichier pour des valeurs de conditions aux bords cas 2D nomme init
            uN[len(x)-1,j]=uN[0,j]
         
            
        uN[1:,1:]=u[1:,1:]+cx*(dt/dx)*(u[:-1,1:]-u[1:,1:])+cy*(dt/dy)*(u[1:,:-1]-u[1:,1:])
        

#message d'erreur too many array