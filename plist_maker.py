import itertools
id = 0
canales = open("canales","r")
ncanales = canales.read().splitlines()
multicast = open("multicast","r")
nmulticast = multicast.read().splitlines()

from lxml import etree
root = etree.Element("root")
doc = etree.ElementTree(root)
track = etree.SubElement(root,'track')

for canal,multi in zip(ncanales,nmulticast):
	title = etree.SubElement(track,'title')
	title.text = str(canal).strip()
	extension = etree.SubElement(track,'extension', application="http://videolan.org/vlc/playlist/0")
	id = id+1
	vlc_id = etree.SubElement(track,'vlc_id')
	vlc_id.text = str(id)
	location = etree.SubElement(track,'location')
	location.text=multi

print(etree.tostring(track,pretty_print=True))