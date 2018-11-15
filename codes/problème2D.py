## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
import init2D
import schema_2D
from mpl_toolkits.mplot3d import Axes3D
import copy
#init2D fichier ou on va chercher la condition initiale definissant le probleme
close('all')

#resolution 2D de l'equation de transport
#cx et cy sont les composantes du vecteur vitesse c
cx=input("Donner une valeur non nulle pour le champ vitesse en x: ")
cx=float(cx)
cy=input("Donner une valeur non nulle pour le champ vitesse en y: ")
cy=float(cx)
#N nombre de mailles
N=input("Choisir le nombre de mailles désires : ")
N=int(N)
#Choix de la condition initiale
f=init2D.i1

#dx le pas d'espace en x
dx=1./N
#dy le pas d'espace en y
dy=1./N
h=1./N
x=arange(0,1+dx,dx) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
y=arange(0,1+dy,dy) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois

u=zeros((len(x),len(y)))
erreur_max=0
#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
#on peut la changer mais par exemple içi on l'impose de cette facon
cfl=0.002

# dt pas de temps
dt=cfl*h

Tmax=0.2 #temps maximal
#Plus Tmax est grand plus l'approximation est bonne

#on doit initialiser la variable au temps t=0
for i in arange(0,len(x)):
    for j in arange(0,len(y)):
        u[i,j]=f(x[i],y[j])
        

#on initialise la valeur initiale du pas de temps
t=0
while t<Tmax :
    #u=s(cx,cy,f,x,y,t,u,uN,dt,dx,dy)
    uold=copy.deepcopy(u)
    u=schema_2D.s1(cx,cy,x,y,t,u,uold,dt,dx,dy)
    t=t+dt
    #•on choisi par exemple une condition aux limites periodiques pour ce probleme
    #♥on connait la solution exacte de la solution alors par exemple on s'en sert pour la condition aux bords 
    #u(x,y,t)=sin(2pi(x-cxt))*sin(2pi(y-cyt))
    for i in arange(0,len(x)):
        u[i,0]=init2D.iexact1(x[i],0,t,cx,cy)
        u[i,len(y)-1]=copy.deepcopy(u[i,0])
    for j in arange (0,len(y)):
        u[0,j]=init2D.iexact1(0,y[j],t,cx,cy)
        u[len(x)-1,j]=copy.deepcopy(u[i,0])
    
    

[X,Y]=meshgrid(x,y)
fig = plt.figure("Approximation de la solution")
my_col = cm.jet(u/np.amax(u))
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,u,rstride=1,cstride=1,facecolors = my_col,linewidth=0, antialiased=False)
title("Approximation de la solution")
show()




