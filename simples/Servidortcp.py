#!/user/bin/python
#-*- coding: utf8 -*-

import socket, os,sys

HOST = 'localhost' # Endereço IP do Servidor
PORT = 5000	   # Porta do Servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Familia do socket criado nesse caso tcp
print "Aguardando Conexão"
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # Pede pro socket zerar seu tempo limite de espera para novas conexoes
s.bind((HOST, PORT)) # Faz a ligação entre endereços e portas
s.listen(1) # Escuta apenas uma conexão

while True:
	conn, addr = s.accept() # Recebe a conexão com o cliente
	print "\nConectado"
	while True:
		msg = conn.recv(1024) # Aceita ate 1024 bytes
		
		if msg=="1":  #Abre o vlc
			print "Abrindo o VLC"
			os.system("vlc")

		elif msg=="2": #Abre o Firefox
			print "Abrindo o Firefox"
			os.system("firefox")

		elif msg=="3": # Abre o GEDIT 
			print "Abrindo o Gedit"
			os.system("gedit")
		if  msg == '\x18' : 
			sys.exit()		

conn.close() # fecha o socket
