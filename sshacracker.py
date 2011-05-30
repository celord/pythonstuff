#!/usr/bin/env python
import sys, math, hashlib, StringIO
from base64 import urlsafe_b64encode as encode
from base64 import urlsafe_b64decode as decode
from time import time, localtime, strftime
'''
Combinancion de dos scripts para crakear una clave SSHA
Scripts (Sin orden alguno)
1  Escrito por makiolo (makiolo@gmail.com) (Licencia GPL)
2  Escrito por Reed O'Brien http://www.openldap.org/faq/data/cache/347.html
'''
#Variables de configuracion 
LONGITUD = 8
ALFABETO = "abcdefghijklmnopqrstuvwxyz0123456789_-."
HASH = '{SSHA}ZQEtePBoN01FyHhqwmHeOQVor++IEyZjLCePPw=='
def variacionesDict(ALFABETO, LONGITUD):
    '''
    Crea cantidada de variaciones de las posibles claves
    en base a las variables de configuracion
    esta funcion no es utilizada para generar el diccionario
    es solo cuando se cambian las variables de configuracion
    y se desea saber la cantidad de variaciones que seran generadas
    '''
    variacionesTotal = 0
    for a in range(LONGITUD):
        producto = 1
        for b in range(a+1):
            producto = producto * len(ALFABETO)
        variacionesTotal = variacionesTotal + producto
    return variacionesTotal

def genTestPass(long,alfabet):
    cont = 0
    passwd = ''
    while long > 0:
        try:
            contadores = []
#Poniendo contadores en cero
            for i in range(long):
                contadores.append(0)

            fin = False
            while not fin:
                captura = StringIO.StringIO()
                for i in range(long):
                    captura.write(str(alfabet[contadores[i]]))
                clave =  captura.getvalue()
                if checkPassword(HASH,clave):
                    print 'clave encontradoa'
                    print clave
                    fin = True
                    long = 0
                    sys.exit(0)
                cont = cont + 1
                actual = long - 1
                contadores[actual] = contadores[actual] + 1
                while (contadores[actual] == len(alfabet)) and not fin:
                    if(actual == 0):
                        fin = True
                    else:
                        contadores[actual] = 0
                        actual = actual - 1
                        contadores[actual] = contadores[actual] + 1
            long = long - 1
        except KeyboardInterrupt:
            print 'Interrunpido por el usuario'
            fin = True
            long = 0

def checkPassword(hash,testPass):
    '''
    Compara el hash dado con el hash que es creado
    a partir del testPass
    '''
    challenge_bytes = decode(hash[6:])
    digest = challenge_bytes[:20]
    salt = challenge_bytes[20:]
    hr = hashlib.sha1(testPass)
    hr.update(salt)
    print 'probando: ' + testPass
    return digest == hr.digest()

genTestPass(LONGITUD,ALFABETO)
