## Tiffanie Carlier
# -*- coding: utf-8 -*-
from pylab import *
import initiale
import schema
#initiale fichier ou on va chercher la condition initiale definissant le probleme
close('all')

#resolution 1D de l'equation de transport
#schema decentré en amont pour c positif et schema decentre en aval pour c négatif
cfl=input("Choix de la condition de cfl entre o et 1 pour la convergeance du schema : ")
cfl=float(cfl)
#Choix de la condition initiale
f=initiale.i3
#Choix du schema 
s=schema.s5

def calcul_erreur(N,c=1,plot=False):
    
    #N nombre de mailles
    #h le pas d'espace
    h=1./N
    x=linspace(0,1,N+1) #x varie de 0 à 1 en augmentant d'un pas de h à chaque fois
    u=zeros((N+1))
    uN=zeros((N+1))
    erreur_max=0
    
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
    if plot:
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
        
        if plot==True : 
            
            if niter%10==0:
                ax.plot(x,uN,'-r')
                ax.plot(x,u_exacte,':b')
            show()
            
    if plot==True : 
        print("Erreur maximale pour la resolution du probleme : %f"%erreur_max)
        #Comparaison des courbes aux derniers temps 
        fig2,ax2 = subplots(1,1)
        ax2.set_title("Comparaison des solutions au temps Tmax")
        ax2.plot(x,uN,'-r',label="solution calculee")
        ax2.plot(x,u_exacte,':b',label="solution exacte")
        #trouver la possiblité d'afficher pour une certaine valeur de t
        legend()
        show()
    return erreur_max

#choix du nombre de mailles
Ns=[200,300,500,700,800,900,1000,2000,4000,5000]
#creation d'un tableau vide
err=[]
for i in arange(0,len(Ns)):
    err.append(calcul_erreur(Ns[i]))
loglog(Ns,err,'-+')
title("Erreur du schema en fonction du pas de temps")
xlabel("nombre de points (log)")
ylabel("erreur max (log)")
show()














