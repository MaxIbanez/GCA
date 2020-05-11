#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Algoritmo para generar contraseñas aleatorias, para distintos usos
ejecutar con python 2 o python 3
"""
import random as rd
import sys


class password():
	def __init__(self):
		self.version = int(sys.version.split()[0].split(".")[0])
		self.cant = 0
		self.clave = ""
	def __main__(self):
		self.printInit()
		self.logicaPrograma()
	def entrada(self):
		print ("\n\tSe recomienda una contraseña de mínimo 8 caracteres")
		cant = int(input("\tTamaño del password a crear: "))
		return cant
	def caracter(self):
		char = chr(rd.randint(33,126))
		return char
	def misClaves(self, clave):
		archivo = open("history.txt","a")
		archivo.write("password:"+clave+"\n")
		print("Clave guardada correctamente")

	def printInit(self):
		print("\t====================================")
		print("\t Generador de contraseñas aleatorio\n\t \t \tby\n\t \tMaximiliano Ibáñez")
		print("\t====================================")
	def logicaPrograma(self):
		self.cant = self.entrada()
		while self.cant<4 or self.cant >128:
			print ("Favor ingresar un numero entre 0 y 128\n")
			cant = self.entrada()
		conteo = 0
		while conteo<self.cant:
			char = self.caracter()
			while char in self.clave:
				char = self.caracter()
			self.clave = self.clave+char
			conteo+=1
		print ("\nContraseña creada exitosamente.\n\nDesea ver en consola(1)\n\to\nver en consola y guardar en archivo(0)")
		opcion = int(input())
		while opcion <0 and opcion>1:
			opcion = int(input("Ingrese opción nuevamente: "))
		if(opcion == 1 ):
			print ("\n"+self.clave)
		else:
			print ("\n"+self.clave)
			self.misClaves(self.clave)



new = password()
new.__main__()