#! /user/bin/python
#!-*- coding:utf-8 -*-
import socket

host = 'localhost' # Endereço IP do Servidor 
port = 5000 	   # Endereço IP do Servidor

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Familia do socket Criado
destino = (host,port) # Conecta com o Servidor
print "1: Abre o vlc"
print "2: Abre o Firefox"
print "3: Abre o Gedit"
print "Para sair use CTRL+X\n"

msg = raw_input("Digite a opção desejada:")
while msg <> '\x18':
	udp.sendto(msg,destino) # envia a mensagem ao destino
	print "1: Abre o vlc"
	print "2: Abre o Firefox"
	print "3: Abre o Gedit"
	print "Para sair use CTRL+X\n"
	msg = raw_input("Digite a opção desejada:")
udp.sendto(msg,destino)
udp.close() # fecha o socket
 
