import os
def fileExists(f):
     try:
         file = open(f)
     except IOError:
         exists = 0
     else:
         exists = 1
     return exists

if  fileExists('/etc/init.d/ruta.sh') == '1':
    #Agregando Rutas
    print 'AGREGAR RUTA:\n'
    fileRutas = open('/etc/init.d/rutas.sh', 'a')
    ruta = raw_input('Red_Destino: ')
    mascara = raw_input('Mascara de Red_Destino: ')
    gateway = raw_input('Gateway: ')

    fileRutas.write('route add -net'+ ruta + 'netmask'+ mascara + 'gw' + gateway)
    fileRutas.close()  
else:
    print 'Creando archivo de rutas en /etc/init.d\n'
    print 'Esto solo se hara una vez si el archivo no existe \n'
    #Creando archivo
    os.chdir('/etc/init.d')
    os.system('touch rutas.sh')
    fileRutas = open('/etc/init.d/rutas.sh', 'w')
    fileRutas.write('#!/bin/bash\n')
    fileRutas.close()
    os.system('chmod +x rutas.sh')
    #Agregando rutas
    fileRutas = open('/etc/init.d/rutas.sh', 'a')
    ruta = raw_input('Red_Destino: ')
    mascara = raw_input('Mascara de Red_Destino: ')
    gateway = raw_input('Gateway: ')

    fileRutas.write('route add -net'+ ruta + 'netmask'+ mascara + 'gw' + gateway)
    fileRutas.close()
    
    
    
