#! /user/bin/pyhton
# -*- coding: utf-8 -*-
import socket,os,sys

host = ''
#host = sys.argv[1] #Endereço IP do Servidor
port = 5000	   # Porta do Servidor

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Familia do Socket Criada
udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print "Aguardando Conexão"
orig = (host, port) # Recebe endereços e portas 
udp.bind(orig) # Faz a ligação entre endereços e portas 


while True:
	msg,cliente = udp.recvfrom(8192) # Recebe ate 1024 bytes

	if msg == '-e':
		print("Abrindo Player")
		os.system("mpg321 -g50 /home/aluno/Documentos/SocketsBroadcast/Racionais\ Mcs\ -\ A\ Vida\ e\ um\ desafio.mp3 &")

	elif msg == '-s':
		print("Fechando o Player")
		os.system("pkill mpg321")
		
	elif msg=='-p':
		print "Desligando"
		os.system("poweroff")
	elif msg == '-r':
		print "Reiniciando"
		os.system("reboot")		

	elif msg == '-x':
		sys.exit()	


#while True :
#        message , address = udp.recvfrom(8192)
#        print 'message (%s) from : %s' % ( str(message), address[0])
#        show_message('message from :'+ str(address[0]) , message)

udp.close()
