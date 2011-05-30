#!/usr/bin/env python
#File addroutes.py
#
#
#      Cesar Garcia
#
#
#

#Import libs
import sys

#Reunir info sobre la ruta

print 'Ingrese la informacion para generar la ruta: \n'
red = raw_input('Red destino: ')
mask = raw_input('Mascara: ')
gw = raw_input('Gateaway: ')

print 'Se ingresara el siguiente comando:'
ruta =  'route add -net ' +red+  ' netmask ' +mask+ ' gw ' +gw
print ruta
routesFile = open('/etc/init.d/rutas.sh','a')
routesFile.write(ruta + '\n')
routesFile.close()
print 'La ruta ha sido tambien agregada en /etc/init.d/rutas.sh'

