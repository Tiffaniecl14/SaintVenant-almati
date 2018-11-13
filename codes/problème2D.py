## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
import init2D
import schema_2D
from mpl_toolkits.mplot3d import Axes3D
#initiale fichier ou on va chercher la condition initiale definissant le probleme
close('all')

#resolution 2D de l'equation de transport
cx=input("Donner une valeur non nulle pour le champ vitesse en x: ")
cx=float(cx)
cy=input("Donner une valeur non nulle pour le champ vitesse en y: ")
cy=float(cx)
#N nombre de mailles
N=input("Choisir le nombre de mailles désires : ")
N=int(N)
#Choix de la condition initiale
f=init2D.i1
#Choix du schema 
s=schema_2D.s1

#dx le pas d'espace en x
dx=1./N
#dy le pas d'espace en y
dy=1./N
h=1./N
x=arange(0,1+dx,dx) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
y=arange(0,1+dy,dy) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois

u=zeros((N+1,N+1))
uN=zeros((N+1,N+1))
erreur_max=0
#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
#on peut la changer mais par exemple içi on l'impose de cette facon
cfl=0.002

# dt pas de temps
dt=cfl*h

Tmax=0.1 #temps maximal
#Plus Tmax est grand plus l'approximation est bonne

#on doit initialiser la variable au temps t=0
u=f(x,y)

#compteur pour l'affichage du resultat
niter=0

#on initialise la valeur initiale du pas de temps
t=0
while t<Tmax :
    u_cal=s(cx,cy,f,x,y,t,u,uN,dt,dx,dy)    
    t=t+dt
    niter=niter+1

[X,Y]=meshgrid(x,y)
fig = plt.figure("Approximation de la solution")
my_col = cm.jet(u/np.amax(u))
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,u_cal,rstride=1,cstride=1,facecolors = my_col,linewidth=0, antialiased=False)
title("Approximation de la solution")
show()




