## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
from matplotlib.pyplot import *
from numpy import *
from mpl_toolkits.mplot3d import Axes3D


import initiale
close("all")
#resolution 1D de l'equation de transport pour un type de schema en particulier
##Affichage du resultat en 3d
#schema decentré en amont pour c positif et schema decentre en aval pour c négatif

c=input("Donner la valeur du champ vitesse : ")
c=int(c)

#N nombre de mailles
N=input("Chiosir le nombre de mailles désires : ")
N=int(N)

#h le pas d'espace
h=1./N
x=linspace(0,1,N+1) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois

#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
cfl=input("Choix de la condition de cfl : ")
cfl=float(cfl)

#dt le pas de temps
dt=cfl*h 
Tmax=0.1 #temps  maximal
#Plus Tmax est petit plus l'approximation est bonne
nt=(Tmax/dt)+1
nt=int(nt)
t=zeros(nt+1)

#on doit initialiser la variable au temps t=0
u=zeros([len(x),nt+1])
u_exacte=zeros([len(x),nt+1])

#valeur de u au temps 0 donné dans le probleme u(x,0)=u0(x)
u[:,0]=initiale.i2(x)

#valeur exacte au temps t =0
u_exacte[:,0]=initiale.i2(x)

#on initialise la valeur initiale du pas de temps
t[0]=0
i=0
while t[i]<Tmax :
    if c>0:
        #on doit apporter une condition sur u(O,t) pour tous temps t
        u[0,:]=initiale.i2(0)
        #calcul de l'approximation à l'aide du schéma choisi u(x,t)
        for j in arange(1,len(x)):
            u[j,i+1]=u[j,i]-c*(dt/h)*(u[j,i]-u[j-1,i])
        i=i+1
        t[i]=t[i-1]+dt
        xi=x-c*t[i]
        #u_exacte=initiale(xi) #u(x,t)=u_0(x-t)
        u_exacte[:,i]=initiale.i2(xi)
        
    if c<0:
        #on doit apporter une condition sur u(O,t) pour tous temps t
        u[-1,:]=0
        #calcul de l'approximation à l'aide du schéma choisi
        for j in arange(0,len(x)-1):
            u[j,i+1]=u[j,i]-c*(dt/h)*(u[j+1,i]-u[j,i])
        t[i+1]=t[i]+dt
        i=i+1
        xi=x-c*t[i]
        #u_exacte=initiale(xi) #u(x,t)=u_0(x-t)
        u_exacte[:,i]=initiale.i2(xi)   
    
[T,X]=meshgrid(t,x)

fig = plt.figure("Approximation de la solution")
my_col = cm.jet(u/np.amax(u))
ax = plt.axes(projection='3d')
ax.plot_surface(X,T,u,rstride=1,cstride=1,facecolors = my_col,linewidth=0, antialiased=False)
title("Approximation de la solution")

fig2 = plt.figure("Solution exacte")
ax2 = plt.axes(projection='3d')
ax2.plot_surface(X,T,u_exacte,rstride=1,cstride=1,cmap='viridis', edgecolor='none')
title("Solution exacte")

show()
    
    