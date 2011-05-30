#!/usr/bin/python
"""
Analiza CDRs ERICSON
re= 
.*(8\d{6})\b.*(8\d{6}).*(\b[a-zA-Z]+\b).*(\b200\d{5})(\d{6})(\d{10})(\d{10})(\d{10})(\d{4})

"""
import sys
import re
import os
"""
Inicializacion de Variables
"""
zerosfile = open('zerotraf.txt','wa')
zerotraf = 0
anystrafile = open('anytraf.txt','wa')
anytraf = 0
promedio_duracion = 0
duracionTotal = 0
duracionMax = 0
duracionMin = 0

"""
Loop para extraer datos de archivos
cdr ERICSON
"""
for file in os.listdir(os.getcwd()):
    archivo = open('file','r')



    
    for linea in archivo.readlines():
        patron = re.compile(
        r"""
        .*?(8\d{7})         #Comienza como sea, luego sigue un num de celular
        .*(\b[a-zA-Z]+\b)   #Cualquier caracter 0 o mas veces luego una palabra 
        .*(\b200\d{5})      #Cualquier cosa,luego 200 + 5 digitos para la fecha
        (\d{6})             #Los siguientes 6 digitos para la hora
        (\d{10})            #Sigueintes 10digitos para el BW total
        (\d{10})            #Siguientes 10digitos para el BW Down
        (\d{10})            #Siguientes 10 digitos para el BW UP
        .*\s(\d+)""",re.VERBOSE)
            
        encontrado = patron.search(linea)
        if encontrado :
            if int(encontrado.group(5)) == 0:

                parsed = encontrado.group(1,2,3,4,5,6,7,8)

                print parsed[0] + '\t' + parsed[1] + '\t'+ parsed[2] + '\t' + \
                parsed[3] + '\t' + parsed[4] + '\t' + parsed[5] + '\t' + \
                parsed[6] + '\t' + parsed[7] + '\t\n'
                #zerosfile.write(parsed[0]+'\t'+parsed[1]+'\t'+parsed[2]+'\t'\
                #+parsed[3]+'\t'+parsed[4]+'\t'+parsed[5]+'\t'+parsed[6]+'\t'+\
                #parsed[7]+'\t\n')

                zerotraf +=1
                  
            else:

                parsed2 = encontrado.group(1,2,3,4,5,6,7,8)

                print parsed2[0] + '\t' + parsed2[1] + '\t' + parsed2[2] + \
                '\t' + parsed2[3] + '\t' + parsed2[4] + '\t' + parsed2[5] + \
                '\t' + parsed2[6] + '\t' + parsed2[7] + '\t\n'

                anytraf += 1
                duracionTotal = duracionTotal + int(parsed2[7])
                promedio = duracionTotal / anytraf
                    
                    
                if duracionMax < int(parsed2[7]):
                    duracionMax = int(parsed2[7])
                    duracionMin = duracionMax
                if duracionMin > int(parsed2[7]):
                        duracionMin = int(parsed2[7])
                    
                    

    print 'Trafico cero=', zerotraf
    print 'Trafico =' , anytraf
    print 'Promedio duracion=', promedio
    print duracionMax
    print duracionMin