import imaplib
def conectar():
    account.login('cgarcia','celord23.')

def readmail():
   account.select(readonly=1)
   cantidad = 0
   tipo, datos = account.search(None, '(UNSEEN)')
   
   for num in datos[0].split(' '):
        tipo, datos = account.fetch(num, '(RFC822.SIZE BODY[HEADER.FIELDS (FROM SUBJECT)])' )
        cantidad += 1
         
        #print 'Mensaje %s\n%s\n' % (num, datos[0][1])
   print 'Usted tiene %d' % (cantidad) + ' mensajes nuevos'
   account.close()

def desconectar():
   account.logout()

if __name__=='__main__':
    account = imaplib.IMAP4( host='icecom.ice.co.cr' )
    

conectar()
readmail()
desconectar()