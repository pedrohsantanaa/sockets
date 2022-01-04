#! /user/bin/python
#-*- coding: utf8 -*-
import socket,sys
#HOST = sys.argv[2]              # Endereco IP do Servidor
#BROADCAST = '192.168.50.255'
PORT = 5000  	       # Porta do Servidor
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Familia do Socket Criado 
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

#s.connect((BROADCAST,PORT)) # Conecta com o endereço e porta 

msg = sys.argv[1]
#s.send (msg) # envia a mensagem
s.sendto(msg, ('<broadcast>' ,PORT))

s.close() # fecha o socket

