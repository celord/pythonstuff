#!/usr/bin/env python
#coding=utf-8

from lxml import etree

et = etree.parse("http://www.bancobcr.com/js/tipoCambio/actual.asp")
root = et.getroot()

for elt in root.getiterator():
    for i in elt.keys():
        if elt.get(i) == '2' and i == 'Moneda' and elt.get('ID') == '1':
            print "Dolar Compra" , elt.get('Valor')
        if elt.get(i) == '2' and i == 'Moneda' and elt.get('ID') == '2':
            print "Dolar Venta" , elt.get('Valor')

