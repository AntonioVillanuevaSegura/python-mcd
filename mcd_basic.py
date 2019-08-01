#!/usr/bin/env python3
# -*- coding: utf-8
"""
Antonio Villanueva Segura
Calculo de MCD de varios numeros
"""
#*******************************************************************************
def esPrimo(num):
    """test si es un numero primo"""
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True  
   
#*******************************************************************************     
def factores_primos (num):
    """crea factorizacion de n. primos """
    factores=[] #factores de este num
    x=1
    while (x <=num+1):
        if esPrimo(x) and num%x==0:        
            factores.append(x)
            num=num/x
            x=1
        x+=1
   
    return factores
#*******************************************************************************   
def mcdv(*num):
    """calculo mcd de argumentos variables """
    existe =True
    factores=[]#Lista de varias dimensiones segun numeros
    mcd=[]#Máximo común divisor a todos los numeros
   
    #Crea una lista con listas de los factores de cada numero
    for n in num:      
        factores.append(factores_primos(n))
   
    for f in factores[0]:#recorre la 1era. factorizacion primer numero.
       
        #Existe f en todas las factorizaciones de los numeros ?
        for index in range(len(num)):
            if f in factores[index]:#Existe f en todas las factorizaciones
                existe=existe and True
            else:
                existe=False
        #Si existe se anade a mcd y lo eliminamos de todas las listas s    
        if existe:
            mcd.append(f)#Se anade el nuevo factor comun
           
            for n in range(1,len(num)):#y se borra de todos
                factores[n].remove(f)
       
        existe=True #Reset del Flag
       
       
    return mcd 
 
#*******************************************************************************
 
""" Bucle principal y zona de Tests"""         
 
#Calculo MCD de tres numeros
print (mcdv(24,36,40)) #2*2=4
print (mcdv(65,45,30)) #5
print (mcdv(12,24,90)) #2*3
print (mcdv(2,3,5))#1
 
#Calculo MCD de 2 numeros
print (mcdv(48,60))#2*2*3=12
 
#Calculo MCD de 1 un numero
print (mcdv(48))
