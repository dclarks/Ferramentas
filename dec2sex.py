#!/usr/bin/python
import sys, getopt, math


lista = (sys.argv)
tam = len(lista)
#print lista

if lista[1]=='help':
    print "O uso do programa deg2sex:"
    print "--------------------------"
    print "dec2sex angulo1 angulo2 angulo3 ..."
    print "--------------------------"
    print "Angulos em formato GG.GGGGGGGGG"
else:
	m = []
	aux = 0
	for i in range(1,tam):
		aux = lista[i]
		aux = float(aux)
		resto, inteiro = math.modf(aux)
		grau = inteiro
		auxx = resto * 60
		resto, minuto = math.modf(auxx)
		segundos = resto * 60
		graus = grau + minuto/100 + segundos/ 10000
		
		m.append(graus)

	tam = len(m)
	for i in range(0,tam):
		print m[i],
