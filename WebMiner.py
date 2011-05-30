#!/usr/bin/env python
# import urlib2 para bajar las paginas web

import urllib2
import sys

httpResponse = urllib2.urlopen(sys.argv[1])
htmlPage = httpResponse.read()

#print htmlPage

#fee el htmlpage a un parser
#se puede usar DOM or Stream parser
#vamos a usar DOM 

from BeautifulSoup import BeautifulSoup

htmlDom = BeautifulSoup(htmlPage)

#tirar el "title" de la pagina

print htmlDom.title.string

#tirar todos los links de la pagina

allLinks = htmlDom.findAll('a',{'href':True})
for link in allLinks:
    print link['href']

#imprimir todos los comentarios de la pagina html

#from BeautifulSoup import Comment

#allComments = htmlDom.findAll( text = lambda text:isinstance(text, Comment))

#for eachComment in allComments:
#    print eachComment

