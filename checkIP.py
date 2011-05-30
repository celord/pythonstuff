#!/usr/bin/python

import GeoIP
import sys
from scapy.all import *

#gi = GeoIP.new(GeoIP.GEOIP_STANDARD)
#gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
gi = GeoIP.open("/opt/geoipdbs/GeoIP.dat",GeoIP.GEOIP_STANDARD)
gio = GeoIP.open('/opt/geoipdbs/GeoIPISP.dat',GeoIP.GEOIP_STANDARD)
ip = sys.argv[1] 


print "Codigo de pais: " + gi.country_code_by_name(ip)
#print gi.last_netmask()
print "Nombre del pais: "+ gi.country_name_by_name(ip)
#print gi.country_code_by_addr(ip)
#print gi.country_name_by_addr(ip)
print "Rango de direccionamiento. ", gi.range_by_ip(ip)
print "ISP: " ,  gio.org_by_addr(ip)


print "Determinando Ruta....: "

ans, unans = traceroute(ip, maxttl=20, timeout=2, dport=80 )

