#!/usr/bin/python
import sys, getopt, math


lista = (sys.argv)
tam = len(lista)
#print lista

if lista[1]=='help':
    print "O uso do programa sex2deg:"
    print "--------------------------"
    print "azimute angulo1 angulo2 angulo3 ..."
    print "--------------------------"
    print "Angulos em formato GG.MMSSSSSS"
else:
	m = []
	aux = 0
	for i in range(1,tam):
		aux = lista[i]
		aux = float(aux)
		resto, inteiro = math.modf(aux)
		grau = inteiro
		#print "Grau decimal: " , grau
		minuto_g = resto * 100
		resto, inteiro = math.modf(minuto_g)
		minuto = inteiro / 60
		#print "Minutos: " , minuto
		segundos_g = resto * 100
		segundos = segundos_g / 3600
		#print "Segundos: " , segundos
		grau_decimal = grau + minuto + segundos
		
		m.append(grau_decimal)

	tam = len(m)
	for i in range(0,tam):
		print m[i],
	

