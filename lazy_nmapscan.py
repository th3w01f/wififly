#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random


lmensj = ["Un puerto de red es una interfaz no física mediante la cual dos máquinas \nintercambian datos a través de un servicio concreto. \nSegún el modelo OSI (Open System Interconnection) su administración se corresponde con la capa 4 (transporte)","Decoy= Significa señuelo y es utilizado para esconder la IP de la maquina origen que esta realizando la exploracion","Fingerprint= Significa identificacion por huella y se utiliza para detectar el sistema operativo de las maquinas que se esta explorando","Spoof= Significa falsificar y va relacionado con algun tipo de servicio o protocolo que se quiera falsear.","Puertos reservados por el sistema = <1024 \nPuertos registrados = [1024:49151] \nPuerto privados o dinamicos = [1025:65535]"]

def escaner(ip):
	#vars
	run = True
	#-
	while(run == True):
		lmrand = random.randint(0,4)
		print("##[(L)azyness (S)ample (F)or (N)map]##")
		print("Tip{")
		print(lmensj[lmrand])
		print("}")
		print("---Puertos predeterminados por algunos servicios---")
		print("Puerto / Servicio \n  21     FTP \n  22     SSH \n  25     SMTP \n  53     DNS \n  80     HTTP \n  110    POP3 \n  143    IMAP \n  443    HTTPS \n  993    IMAPSSL \n  995    POPSSL")
		print("""{
			(1)-Saber_que_puertos_tengo_abiertos.     (7)-TCP-ACK[sA]       (14)-VerEstadodePuerto[netstat]
			(2)-Basic_Scan[sS Pn O].                  (8)-Window_scanTCP[sW] 
			(3)-Scan_UDP[sU].                         (9)-Maimon_scan[sM]
			(4)-Scan_TCPNULL[sN]                      (10)-TCP_adaptative_scan--scanflags[URG ACK PSH RST SYN FIN]
			(5)-Scan_XMAS[sX]                         (11)-Ip_scan(sO)
			(6)-scan_FIN[sF]                          (12)-<user>:<pass>@<server>:<port>(b)
			(q)-salir                                 (13)-IdleScan $[Ej. nmap -sI zombie_host target_host]$[sI]
			}""")
		usrAns = input('ingrese una opcion > ')
		if(usrAns == '1'):
			os.system('sudo netstat -tuna')
			print("#[Lista de puertos UDP/TCP activos]#")
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '2'):
			os.system('sudo nmap -A -T4 -sS -Pn -O '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '3'):
			os.system('sudo nmap  -sU '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '4'):
			os.system('sudo nmap  -sN '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '5'):
			os.system('sudo nmap  -sX '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '6'):
			os.system('sudo nmap -sF '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '7'):
			os.system('sudo nmap -sA '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '8'):
			os.system('sudo nmap -sW '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '9'):
			os.system('sudo nmap -sW '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '10'):
			flags = input('ingresa las flags > ')
			os.system('sudo nmap --scanflags '+flags+' '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '11'):
			os.system('sudo nmap  -sO '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '12'):
			print("$[Ej. nmap <user>:<pass>@<server>:<port>]$")
			user = input('user > ')
			psw = input('psw > ')
			port = input('port > ')
			os.system('sudo nmap -Pn -b '+user+':'+psw+'@'+ip+':'+port)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '13'):
			os.system('sudo nmap -sI -Pn '+ip)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '14'):
			port = input('Nro del Puerto > ')
			os.system('sudo netstat -putan | grep '+port)
			usrAns = input('(s)alir o (c)ontinuar ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == 'q'):
			run = False
