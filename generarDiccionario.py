#!/usr/bin/python
#
# :: Invasion Tux
# :: Script realizado por makiolo (makiolo@gmail.com) (Licencia GPL)
# :: Ultima version : 
#http://blogricardo.wordpress.com/2008/12/28/script-para-generar-diccionarios-de-fuerza-bruta/
# :: Dependencias : python
#

import sys, math, StringIO
from time import time, localtime, strftime

########################### CONFIGURACION #########################

LONGITUD = 6
ALFABETO = "abcdefghijklmnopqrstuvwxyz0123456789_-."

####################################################################

########################## FUNCIONES ###############################
def getVariacionesConRepeticion(ALFABETO , LONGITUD):
  sumatorio = 0
  for i in range(LONGITUD):
    producto = 1
    for j in range(i+1):
      producto = producto * len(ALFABETO)
    sumatorio = sumatorio + producto
  return sumatorio
####################################################################

##################### VARS AUXILIARES ##############################
DEBUG = True
VERBOSE = False
#variacionesConRepeticion = getVariacionesConRepeticion(ALFABETO , 
#LONGITUD)
inicioReloj = time()
cont = 0
progreso = 0
####################################################################

while LONGITUD > 0:
  try:
    contadores = []                                                     
# ponemos los contadores a 0
    for i in range(LONGITUD):
      contadores.append(0)

    fin = False
    while not fin:
      if DEBUG == True:
        file = StringIO.StringIO()
        for i in range(LONGITUD):
            file.write(ALFABETO[contadores[i]])
#           sys.stdout.write(ALFABETO[contadores[i]])
#       sys.stdout.write("\n")
        clave = file.getvalue()
        print(clave)
      if VERBOSE == True:
        if (cont % 600000 == 0) and (cont != 0):
          progreso = cont*100.0/variacionesConRepeticion                
# porcentaje hasta ahora
          progreso = round(progreso , 2)
          finReloj = time() - inicioReloj                               
# finReloj es lo que esta tardando el calculo
          velocidad = cont / finReloj                                   
# palabras procesadas por segundo
          velocidad = round(velocidad , 2)
          estimado = finReloj * variacionesConRepeticion / cont         
# es lo que se estima en realizar todo el proceso
          restante = estimado - finReloj                                
# es lo que se estima en realizar lo restante
          restante = restante / 60 / 60                                 
# lo pasamos a horas
          restante = round(restante , 2)
          sys.stderr.write(str(progreso)+"% - Quedan "+str(restante) \
                  +"horas. La velocidad es de "+str(velocidad)+" palabras/seg\n")

      cont = cont + 1
      actual = LONGITUD - 1                                             
# Pongo actual a la derecha del todo
      contadores[actual] = contadores[actual] + 1                       
# Sumo 1 a las unidades

      while(contadores[actual] == len(ALFABETO)) and not fin:           
# Propago el carry
        if(actual == 0):
          fin = True                                                    
# FIN
        else:
          contadores[actual] = 0                                        
# reinicia el actual contador
          actual = actual - 1                                           
# avanza a la izquierda
          contadores[actual] = contadores[actual] + 1                   
# y le sumo 1
    
    LONGITUD = LONGITUD - 1                                             
# combinaciones para uno menos
    
  except KeyboardInterrupt:
    sys.stderr.write("Interrumpido por el usuario\n")
    fin = True                                                          
# Fuerzo las condiciones de salida
    LONGITUD = 0

if VERBOSE == True:
  sys.stderr.write("Terminado al "+str(progreso)+"% - Realizadas "+str(cont)) 
