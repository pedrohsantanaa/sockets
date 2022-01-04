#! /user/bin/pyhton
# -*- coding: utf-8 -*-
import socket,os,sys

host = "localhost" #Endereço IP do Servidor
port = 5000	   # Porta do Servidor

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Familia do Socket Criada
print "Aguardando Conexão"
orig = (host, port) # Recebe endereços e portas 
udp.bind(orig) # Faz a ligação entre endereços e portas 

while True:
	msg,cliente = udp.recvfrom(1024) # Recebe ate 1024 bytes

	if msg=="1": 
		print "Abrindo o vlc"
		os.system("vlc") # Abre o vlc 

	elif msg=="2":
		print "Abrindo o Firefox"
		os.system("firefox") #Abre o Firefox 


	elif msg=="3": 
		print "Abrindo o Gedit"
		os.system("gedit") # Abre o Gedit  
	
	if msg == '\x18':	
		sys.exit()
udp.close()
