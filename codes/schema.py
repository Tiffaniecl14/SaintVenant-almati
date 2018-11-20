#-*- coding: utf-8 -*-
#module des differents schema possible pour la resolution de l'equation de transport
from pylab import *

#schema decentre
def s1(c,f,x,t,u,uN,dt,h): #schema stable car tient compte du signe de c
    if c>0:
            uN[0]=f(x[0]-c*t) 
            uN[1:]=u[1:]-c*(dt/h)*(u[1:]-u[0:-1])
    if c<0:
            uN[-1]=f(x[-1]-c*t)
            uN[:-1]=u[:-1]-c*(dt/h)*(u[1:]-u[:-1])
    return uN

#schema centre de Richardson
def s2(c,f,x,t,u,uN,dt,h): #schema instable car ne tient pas compte du signe de c
    uN[0]=f(x[0]-c*t) 
    uN[1:-1]=u[1:-1]-c*(dt/(2*h))*(u[2:]-u[:-2])
    uN[-1]=f(x[-1]-c*t)
    return uN
    
#schema de Lax-Wendroff
def s3(c,f,x,t,u,uN,dt,h): 
    uN[0]=f(x[0]-c*t) 
    uN[1:-1]=u[1:-1]-c*0.5*(dt/h)*(u[2:]-u[:-2])+(c*c*dt*dt/(h*h))*(u[2:]-2*u[1:-1]+u[:-2])
    uN[-1]=f(x[-1]-c*t)
    return uN
    
#schema d'Euler explicite en aval
def s4(c,f,x,t,u,uN,dt,h): 
    uN[:-1]=u[:-1]-c*(dt/h)*(u[1:]-u[:-1])
    uN[-1]=f(x[-1]-c*t)
    return uN
    
#schema de Lax-Friedrichs
def s5(c,f,x,t,u,uN,dt,h): 
    uN[0]=f(x[0]-c*t) 
    uN[1:-1]=0.5*(1-c*dt/h)*u[2:]+0.5*(1+c*dt/h)*u[:-2]
    uN[-1]=f(x[-1]-c*t)
    return uN