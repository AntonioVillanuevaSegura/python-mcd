# -*- coding: utf-8 -*-
"""
Antonio Villanueva Segura
Calculo de mcd por Euclides 
y calculo de mcd varios numeros 
"""
def mcd (num1,num2):
	"""Calculo mcd por euclides"""	
	if num1<num2:#Swap if num2>
		num1,num2=num2,num1
		
	while (num2!=0):	
		a=num1		
		num1=num2
		num2=a%num2
		
	return num1
	
def mcd_varios(*num):
	"""calculo mcd de varios numeros """
	tmp=num[0]
	for n in num:		
		tmp=mcd(tmp,n)
	return tmp

#Bucle principal y test 
	
print (mcd_varios(2366,273))#Res=91 test 2 numeros
print (mcd_varios(24,36,40))#Res=4 test 3 numeros
print (mcd_varios(20,24,30))#Res=2 test 3 numeros
print (mcd_varios(1,3,5))#Res=1 test 3 numeros
print (mcd_varios(273,2366))#Res=91 test 2 numeros
print (mcd_varios(18,15,8))#Res=1 test 3 numeros

		
	
