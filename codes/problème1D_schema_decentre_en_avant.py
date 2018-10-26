## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
import initiale
#initiale fichier ou on va chercher la condition initiale definissant le probleme

#resolution 1D de l'equation de transport sur le domaine ouvert (0,1)
#schema decentré en avant 
#le schéma est adapté au cas ou la valeur du champ vitesse est négative 
print("Le schema de resolution utilisé est adpté à un vecteur vitesse négatif")
c=input("Donner la valeur du champ vitesse : ")
c=int(c)
#N nombre de mailles
N=input("Choisir le nombre de mailles désirés : ")
N=int(N)
#h le pas d'espace de taille N
h=1./N
x=arange(0,1+h,h) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
#x est de taille N+1

#initialisation d'un vecteur pour la solution calculé
u=zeros((N+1))

#pas de temps
#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
cfl=input("Choix de la condition de cfl : ")
cfl=float(cfl)
#on defini ainsi le pas de temps en fonction du pas d'espace est de la cfl
dt=cfl*h 

Tmax=0.1 #temps d'integration maximal pour la boucle tant que 
#Plus Tmax est grand plus l'approximation est grande 

#on doit initialiser la variable au temps t=0 ie u0(x)
u=initiale.i2(x)
#on initialise la valeur initiale du pas de temps
t=0
while t<Tmax : 
    for j in arange(1,N-1):
        u[j]=u[j]-c*(dt/h)*(u[j+1]-u[j])
    #condition au bord sur le probleme
    #ici le bord de Omega est 1 donc donné exacte en 1
    u[N]=initiale.i2(x[N]-c*t)
    t=t+dt
    xi=x-c*t
    #u_exacte=initiale(xi) #u(x,t)=u_0(x-ct)
    u_exacte=initiale.i2(x-c*t)
    
    figure(1)
    title("Resultat de l'approximation au differents temps considérés'")
    plot(x,u,'-r')
    plot(x,u_exacte,':b')
#Comparaison des courbes aux derniers temps 
figure(2)
title("Comparaison des solutions au temps Tmax")
plot(x,u,'-r',label="solution calculé")
plot(x,u_exacte,':b',label="solution exacte")
    #trouver la possiblité d'afficher pour une certaine valeur de t
legend()
show()