## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
import initiale
import schema
#initiale fichier ou on va chercher la condition initiale definissant le probleme
close('all')

#resolution 1D de l'equation de transport
#schema decentré en amont pour c positif et schema decentre en aval pour c négatif
c=input("Donner une valeur non nulle pour le champ vitesse : ")
c=float(c)

#N nombre de mailles
N=input("Choisir le nombre de mailles désires : ")
N=int(N)
#Choix de la condition initiale
f=initiale.i1
#Choix du schema 
s=schema.s1

#h le pas d'espace
h=1./N
x=arange(0,1+h,h) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
u=zeros((N+1))
uN=zeros((N+1))
erreur_max=0
#on doit choisir le pas de temps de maniere a ce que la condition de cfl soit au plus egale à 1
cfl=0.002

# dt pas de temps
dt=cfl*h

Tmax=0.1 #temps maximal
#Plus Tmax est grand plus l'approximation est bonne

#on doit initialiser la variable au temps t=0
u=f(x)

#compteur pour l'affichage du resultat
niter=0

#on initialise la valeur initiale du pas de temps
t=0
fig,ax = subplots(1,1)
ax.set_title("Resultat de l'approximation aux differents temps consideres")
while t<Tmax :
    u=s(c,f,x,t,u,uN,dt,h)    
    t=t+dt
    niter=niter+1

    #u_exacte=initiale(xi) #u(x,t)=u_0(x-t)
    u_exacte=f(x-c*t)
    
    #Calcul de l'erreur
    erreur=norm(u_exacte-uN,2)
    if erreur>erreur_max :
        erreur_max=erreur
        
    if niter%10==0:
        ax.plot(x,uN,'-r')
        ax.plot(x,u_exacte,':b')
show()

print("Erreur maximale pour la resolution du probleme : %f"%erreur_max)
#Comparaison des courbes aux derniers temps 
fig2,ax2 = subplots(1,1)
ax2.set_title("Comparaison des solutions au temps Tmax")
ax2.plot(x,uN,'-r',label="solution calculee")
ax2.plot(x,u_exacte,':b',label="solution exacte")
#trouver la possiblité d'afficher pour une certaine valeur de t
legend()
show()
    
