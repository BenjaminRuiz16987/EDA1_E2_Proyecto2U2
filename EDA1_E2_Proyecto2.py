# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:32:27 2019

@author: sasuke16987
"""
def quitarEspacios(cadena,letra):

	return cadena.replace(letra,"")


cadena=str(input("Inserte su cadena, leerá hasta que haya un * ; si sigue escribiendo no guarda los despues del *:\n"))
ast=cadena.find("*")
if(ast==-1):
    print("No insertó *. Reinicie el Programa")
    exit
A=cadena[0:ast]

AsE= quitarEspacios(A," ")


