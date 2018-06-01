#!/usr/bin/env python
#-*- coding: utf-8 -*-

from argparse import ArgumentParser as ArgP
import os

#gb
run = True
rundc = True
vdev = ""

#funcs

# muestra las caracteristicas y estadisticas del dispositivo inalambrico y hace la pregunta del millon
def init(vdev):
	os.system("clear")
	print(" \n \n \n ")
	print("[Caracteristicas inalambricas del dispositivo] \n ")
	os.system("sudo iwconfig ")
	print("[Estadisticas de trafico de los dispositivos de red] \n ")
	os.system("sudo ip -s link")
#---

# muestra los valores de la interfaz inalambrica
def dvinf(vdev):
	print("---#---[SCANing APs]---#---")
	os.system("sudo iwlist "+vdev+" scanning")
	print("---#---[FREquency]---#---")
	os.system("sudo iwlist "+vdev+" frequency")
	print("---#---[BitRate]---#---")
	os.system("sudo iwlist "+vdev+" rate")
	print("---#---[Keys]---#---")
	os.system("sudo iwlist "+vdev+" keys")
	print("---#---[PoWer]#---")
	os.system("sudo iwlist "+vdev+" power")
	print("---#---[TX-Power]---#---")
	os.system("sudo iwlist "+vdev+" txpower")
	print("---#---[retry]---#---")
	os.system("sudo iwlist "+vdev+" retry")
	print("---#---[Event]---#---")
	os.system("sudo iwlist "+vdev+" event")
	print("---#---[Auth]---#---")
	os.system("sudo iwlist "+vdev+" auth")
	print("---#---[WPA-keys]---#---")
	os.system("sudo iwlist "+vdev+" wpakeys")
	print("---#---[genie]---#---")
	os.system("sudo iwlist "+vdev+" genie")
	print("---#---[MODulation]---#---")
	os.system("sudo iwlist "+vdev+" modulation")
	print("---#---[nombre de la tarjeta inalambrica]---#---")
	os.system("sudo lspci -s 02:00.0")
	print("---#---[ip]---#---")
	os.system("sudo ip addr show "+vdev)
#---

#cambia la ip de la interfaz inalambrica
def setip(vdev):
	usrAns = input("([e]liminar o [a]gregar) IP")
	if(usrAns == 'a'):
		newip = input("introduzca la nueva ip local > ")
		os.system("sudo ip addr add "+newip+"/32 dev "+vdev)
	if(usrAns == 'e'):
		eraseip = input("que direccion ip desea eliminar ?> ")
		os.system("sudo ip addr del "+eraseip+"/32 dev  "+vdev)
#---

#administra la interfaz inalambrica [ON|Off]
def mdev(vdev):
	print("##[(p)ower|(pr)omiscuic|(m)tu]##")
	usrAns = input("escoja una opcion > ")
	if(usrAns == "p"):
		usrAns = input("[on|off]> ")
		if(usrAns == 'on'):
			os.system("sudo ip link set dev "+vdev+" up")
		if(usrAns == 'off'):
			os.system("sudo ip link set dev "+vdev+" down")
	if(usrAns == "pr"):
		usrAns = input("usar el dispositivo inalambrico en modo promiscuo pillin [on|off]> ")
		if(usrAns == "on"):
			os.system("sudo ip link set "+vdev+" promisc on")
		if(usrAns == "off"):
			os.system("sudo ip link set "+vdev+" promisc off")
	if(usrAns == "m"):
		usrAns = input("ingresa el valor del mtu > ")
		os.system("sudo ip link set "+vdev+" mtu "+usrAns)
#---

# enruta las direcciones inalambricas virtuales del sistema
def grout(vdev):
	print("""
	agregra puerta de enlace predeterminada para todas las direcciones virtuales | (a)dd_default_(g)ateway_for_(a)ll
	agregar una direccion de red en la puerta de enlace predt | (s)et_local_(a)ddress_via_(g)ateway
	agrega a la interfaz inalambrica una direccion virtual | (v)irtual_(a)ddress_(d)ev
	borra una direccion perteneciente a la puerta de enlace p. | (e)rase_(l)ocal_(a)ddress_from_(g)ateway
	remplazar la direccion ip de la interfaz inalambrica | (r)emplace_(i)p_(d)evice
	Muestra los nodos que existen entre su direccion a buscar | (groot)
	""")
	usrAns = input("opcion > ")
	if(usrAns == "aga"):
		os.system("sudo ip route add default via 192.168.1.1 "+vdev)
	if(usrAns == "sag"):
		os.system("sudo ip route add 192.168.1.0/24 via 192.168.1.1")
	if(usrAns == "vad"):
		os.system("sudo ip route add 192.168.1.0/24  "+vdev)
	if(usrAns == "elag"):
		os.system("sudo ip route delete 192.168.1.0/24 via 192.168.1.1")
	if(usrAns == "rid"):
		os.system("sudo ip route replace 192.168.1.0/24 "+vdev)
	if(usrAns == "groot"):
		os.system("sudo ip route get 192.168.1.5")
#---

parser = ArgP(
	prog="wififly.py",
	description="~°|navaja suiza electroestatica|°~",
	epilog="{%[herramienta para la auditoria de redes inalambricas]%}"
)

#parser.add_argument("device", metavar="D", type=str,action="store_const", dest="vdev", help="especifica el dispositivo inalambrico")
parser.add_argument("-dvinf" ,"--devinf", action="store_true", help="muestra informacion sobre el dispositivo inalambrico")
parser.add_argument("-setip", "--setupip", action="store_true", help="agrega o elimina una  direccion ip local  para el disp.")
parser.add_argument("-mdev", "--moddev", action="store_true", help="Enciende o Apaga el disp. Inalambrico")
parser.add_argument("-rout","--grooute", action="store_true", help="enruta tus direcciones inalambricas entre tuneles y gateways ")


args = parser.parse_args()


if(__name__ == "__main__"):
	init(vdev)
	vdev = input("ingresa el nombre de la interfaz inalambrica > ")
	if(args.devinf):
		dvinf(vdev)
	if(args.setupip):
		setip(vdev)
	if(args.moddev):
		mdev(vdev)
	if(args.grooute):
		grout(vdev)
