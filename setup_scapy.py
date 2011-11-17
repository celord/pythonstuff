#!/usr/bin/python
#title			:setup_scapy.py
#description	:Script para instalar scapy en un sistema ubuntu nuevo.
#author			:Cesar Garcia
#date			:20111103
#version		:0.1
#usage			:python cpe.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import sys,subprocess

LATEST_SCAPY = "http://www.secdev.org/projects/scapy/files/scapy-latest.zip"

def usage():
    print "Instala scapy en un sistema Ubuntu nuevo, requeire conexion a internet"
   
def dependencies():
    """ Encontrar dependencias del sistema"""
    proc = subprocess.Popen("dpkg --status python-setuptools | grep 'ok installed'", shell=True, stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]

    if "installed" in stdout_value:
        print "Todos los paquetes necesarios estan instalados"
        print "Descargardo scapy..."
        install_scapy()

    else:
        proc = subprocess.Popen("sudo apt-get install -y python-setuptools",  shell=True,  stdout=subprocess.PIPE)
        print proc.communicate()[0]
        
    print "Instalando manejador de modulos python: pip"
    proc = subprocess.Popen("sudo easy_install pip",  shell=True,  stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    
    print "Instalando interprete avanzado de python: ipython"
    proc = subprocess.Popen("sudo easy_install ipython",  shell=True, stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]

def install_scapy():
    """Descarga la ultima version de scapy"""
    print "Instalando scapy..."
    proc = subprocess.Popen("wget "+ LATEST_SCAPY, shell=True,  stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print stdout_value
    
    print "unziping..."
    proc = subprocess.Popen("unzip scapy-latest.zip",  shell=True,  stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print stdout_value
    
    print "mv dir.."
    proc = subprocess.Popen("mv scapy-2* scapy-latest",  shell=True,  stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print stdout_value
    
    print "installing..."
    proc = subprocess.Popen("cd scapy-latest && sudo ./setup.py install", shell=True,  stdout=subprocess.PIPE)
    stdout_value = proc.communicate()[0]
    print stdout_value
    
if __name__ == '__main__':
    dependencies()

