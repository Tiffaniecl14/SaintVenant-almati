## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
from matplotlib.pyplot import *
from numpy import *
from mpl_toolkits.mplot3d import Axes3D


import initiale
#initiale fichier ou on va chercher la condition initiale

#resolution 1D de l'equation de transport
##Affichage du resultat en 3d
#schema decentré en amont
#Ici le schema est particulierement adaptéau cas c positif
c=input("Donner la valeur du champ vitesse : ")
c=int(c)
#N nombre de mailles
N=input("Chiosir le nombre de mailles désirés : ")
N=int(N)
#h le pas d'espace
h=1./N
x=arange(0,1+h,h) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
#pas de temps
#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
cfl=input("Choix de la condition de cfl : ")
cfl=float(cfl)
#dt le pas de temps
dt=cfl*h 
Tmax=0.1 #temps d'integration maximal
#Plus Tmax est petit plus l'approximation est bonne
t=zeros(int(Tmax/dt)+2)
#on doit initialiser la variable au temps t=0
u=zeros([N+1,int(Tmax/dt)+2])
u_exacte=zeros([N+1,int(Tmax/dt)+2])
#valeur de u au temps 0
u[:,0]=initiale.i2(x)
#valeur exacte au temps t =0
u_exacte[:,0]=initiale.i2(x)
#on initialise la valeur initiale du pas de temps
t[0]=0
i=0
while t[i]<Tmax :
    #on doit apporter une condition sur u(O,t) pour tous temps t
    u[0,:]=initiale.i2(0)
    #calcul de l'approximation à l'aide du schéma choisi
    for j in arange(1,N+1):
        u[j,i+1]=u[j,i]-c*(dt/h)*(u[j,i]-u[j-1,i])
    i=i+1
    t[i]=t[i-1]+dt
    xi=x-c*t[i]
    #u_exacte=initiale(xi) #u(x,t)=u_0(x-t)
    u_exacte[:,i]=initiale.i2(xi)
    
[T,X]=meshgrid(t,x)

fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot_surface(X,T,u,rstride=1,cstride=1,cmap='viridis', edgecolor='none')
fig2 = plt.figure(2)
ax2 = plt.axes(projection='3d')
ax2.plot_surface(X,T,u_exacte,rstride=2,cstride=2,cmap='viridis', edgecolor='none')
show()
    
    