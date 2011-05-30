#!/usr/bin/env python
#
#       sula.py
#
#       IVR-Sula
#
#  Jean Chassoul - 3/9/08
#
#


#  Import module required.
import datetime
import MySQLdb
import pyagi

#  IVR variables
ident_id = 0		# 49 = Cedula, 50 = Familiar
phone_id = 0		# 49 = Fijo, 50 = Celular
num_phone = 0		# Numero de Telefono
num_ident = 0		# Numero de Cedula
sexo_id = 0		# Genero
dept_id = 0		# Departamento/Provincia
num_codigo = 0		# Codigo Magico

#  MySQL connection
host = 'localhost'
user = 'root'
password = '*****'
database = 'ivrs'

db=MySQLdb.connect(host,user,password,database)
cursor = db.cursor()

#  Other stuff
count = 0
tcount = 0
confirm = 0

#  Bienvenida & Identificacion:
while count <= 2:
	
	if tcount == 3:
		break
	else:
		pass
	
	ident_id = pyagi.streamfile ('sula-bienv-larga', '1,2')
	
	if ident_id.find('=49') != -1:
                
                ident_id = 'A'
		
		while tcount <= 2:
			num_ident = pyagi.getdata ('sula-marca-ced', 36000, 13).split("=")[1]
			
			if len(num_ident) <= 12 or num_ident.find('*') != -1:
				pyagi.streamfile ('sula-cedu-11digs', '""')
				count += 1
				tcount += 1
				
			elif num_ident == '-1':
				count = 3

			else:
				pyagi.streamfile ('sula-el-num-ud-marco', '""')
				pyagi.salpha (num_ident)
				confirm = pyagi.streamfile ('sula-si1-no2', '1,2')
								
				if confirm.find('=49') != -1:
					tcount = 3
				elif confirm.find('=50') != -1:
					tcount += 1
					count += 1
				else:
					pyagi.streamfile ('sula-opcion-inv', '""')
					tcount += 1
					count += 1
					
		confirm = 0
						
		
	elif ident_id.find('=50') != -1:
		
                ident_id = 'M'                
		
		while tcount <= 2:
			num_ident = pyagi.getdata ('sula-marca-ced-famili', 36000, 13)
			num_ident = num_ident.split("=")[1]
			
			if len(num_ident) <= 12 or num_ident.find('*') != -1:
				pyagi.streamfile ('sula-cedu-11digs', '""')
				count += 1
				tcount += 1
				
			elif num_ident == '-1':
				count = 3			
				
			else:
				pyagi.streamfile ('sula-el-num-ud-marco', '""')
				pyagi.salpha (num_ident)
				confirm = pyagi.streamfile ('sula-si1-no2', '1,2')
								
				if confirm.find('=49') != -1:
					tcount = 3
				elif confirm.find('=50') != -1:
					tcount += 1
					count += 1
				else:
					pyagi.streamfile ('sula-opcion-inv', '""')
					tcount += 1
					count += 1
			
		confirm = 0
		
		
	elif ident_id.split("=")[1] == '-1':
		pyagi.hangup ()
	elif ident_id.split("=")[1] == '0':
		count += 1
				
	else:
		pyagi.streamfile ('sula-opcion-inv', '""')
		count += 1
	

#  Primer Hangup
if count >= 2:
	pyagi.hangup ()
else:
	pass

# Counter Reset:
count = 0
tcount = 0

# !@#$%^&*()??
cursor.execute ('''select * from ivrsula where num_ident = %s''', num_ident)
sql_reg = cursor.fetchall()

if len(sql_reg)>= 1:
	
	# Registro de Codigo Magico:
    while count <= 4:
	
	    if tcount >= 3:
		    break
	    else:
		    pass
	
	    num_codigo = pyagi.getdata ('sula-marca-codig', 36000, 5).split("=")[1]
	
	    if len(num_codigo) <= 4 or num_codigo.find('*') != -1:
		    pyagi.streamfile ('sula-opcion-inv', '""')
		    count += 1
		
	    elif num_codigo == '-1':
		    pyagi.hangup ()
		
	    else:
	    	createdate = datetime.datetime.now().strftime("%y%m%d%H%M%S")
	    	cursor.execute('''insert into ivrsula values (%s, %s, %s, %s, %s, %s, %s, %s)''',
	    	              (num_codigo, num_ident, sql_reg[0][2], ident_id, sql_reg[0][4], sql_reg[0][5], sql_reg[0][6], createdate))
	    	tcount += 1
	
	    while tcount <= 2:
		    confirm = pyagi.streamfile ('sula-preg-otro-cod', '1,2')
		
		    if confirm.find('=49') != -1:
			    break
		    elif confirm.find('=50') != -1:
			    tcount = 3
		    elif confirm.find('-1') != -1:
			    tcount = 3
		    else:
			    pyagi.streamfile ('sula-opcion-inv', '""')
	# Gracias por llamar... etc..:
    pyagi.streamfile ('sula-salida-thx', '""')
    pyagi.hangup ()

else:
	pass


# Counter Reset:
count = 0
tcount = 0

####SHIT#$%^&*()_ DIE!!!

while count <= 2:
	
	if tcount == 3:
		break
	else:
		pass
	
	phone_id = pyagi.streamfile ('sula-fijo1-cel2', '1,2')
	
	if phone_id.find('=49') != -1:

                phone_id = 'F'
		
		while tcount <= 2:
			num_phone = pyagi.getdata ('sula-marca-numphone', 36000, 7).split("=")[1]
			
			if len(num_phone) <= 6 or num_phone.find('*') != -1:
				pyagi.streamfile ('sula-tfijo-7digs', '""')
				count += 1
				tcount += 1
				
			elif num_phone == '-1':
				count = 3

			else:
				pyagi.streamfile ('sula-el-num-ud-marco', '""')
				pyagi.salpha (num_phone)
				confirm = pyagi.streamfile ('sula-si1-no2', '1,2')
								
				if confirm.find('=49') != -1:
					tcount = 3
				elif confirm.find('=50') != -1:
					tcount += 1
					count += 1
				else:
					pyagi.streamfile ('sula-opcion-inv', '""')
					tcount += 1
					count += 1
					
		confirm = 0
						
		
	elif phone_id.find('=50') != -1:

                phone_id = 'C'
				
		while tcount <= 2:
			num_phone = pyagi.getdata ('sula-marca-numphone', 36000, 8).split("=")[1]
			
			if len(num_phone) <= 7 or num_phone.find('*') != -1:
				pyagi.streamfile ('sula-tcelu-8digs', '""')
				count += 1
				tcount += 1
				
			elif num_phone == '-1':
				count = 3			
				
			else:
				pyagi.streamfile ('sula-el-num-ud-marco', '""')
				pyagi.salpha (num_phone)
				confirm = pyagi.streamfile ('sula-si1-no2', '1,2')
								
				if confirm.find('=49') != -1:
					tcount = 3
				elif confirm.find('=50') != -1:
					tcount += 1
					count += 1
				else:
					pyagi.streamfile ('sula-opcion-inv', '""')
					tcount += 1
					count += 1
			
		confirm = 0
		
		
	elif phone_id.split("=")[1] == '-1':
		pyagi.hangup ()
	elif phone_id.split("=")[1] == '0':
		count += 1
				
	else:
		pyagi.streamfile ('sula-opcion-inv', '""')
		count += 1
	

#  Segundo Hangup
if count >= 2:
	pyagi.hangup ()
else:
	pass

# Counter Reset:
count = 0
tcount = 0


#  Tipo de Genero de sexo sexual...:
while count <= 2:
	sexo_id = pyagi.streamfile ('sula-preg-genero', '1,2')
	
	if sexo_id.find('=-1') != -1:
                pyagi.hangup ()

        elif sexo_id.find('=49') != -1:
                sexo_id = 'F'
		count = 3
	elif sexo_id.find('=50') != -1:
                sexo_id = 'M'
		count = 3
        
	else:
		pyagi.streamfile ('sula-opcion-inv','""')
		count += 1

if sexo_id.find('F') != -1 or sexo_id.find('M') != -1:
	pass
else:
	pyagi.hangup ()
      
# Counter Reset:
count = 0
tcount = 0


# Registro de Departamento/Provincia
while count <= 2:
    dept_id = pyagi.getdata ('sula-dep-donde-vivess', 36000, 1).split("=")[1]
    
    if dept_id.find('*') == -1 and eval(dept_id) <= 6 and eval(dept_id) != 0:
        count = 3
    else:
        pyagi.streamfile ('sula-opcion-inv', '""')


# Registro de Codigo Magico:
while count <= 4:
	
	if tcount >= 3:
		break
	else:
		pass
	
	num_codigo = pyagi.getdata ('sula-marca-codig', 36000, 5).split("=")[1]
	
	if len(num_codigo) <= 4 or num_codigo.find('*') != -1:
		pyagi.streamfile ('sula-opcion-inv', '""')
		count += 1
		
	elif num_codigo == '-1':
		pyagi.hangup ()
		
	else:
		createdate = datetime.datetime.now().strftime("%y%m%d%H%M%S")
		cursor.execute('''insert into ivrsula values (%s, %s, %s, %s, %s, %s, %s, %s)''',
		              (num_codigo, num_ident, num_phone, ident_id, phone_id, sexo_id, dept_id, createdate))
		tcount += 1
	
	while tcount <= 2:
		confirm = pyagi.streamfile ('sula-preg-otro-cod', '1,2')
		
		if confirm.find('=49') != -1:
			break
		elif confirm.find('=50') != -1:
			tcount = 3
		elif confirm.find('-1') != -1:
			tcount = 3
		else:
			pyagi.streamfile ('sula-opcion-inv', '""')
		
# Gracias por llamar... etc..:
pyagi.streamfile ('sula-salida-thx', '""')
pyagi.hangup ()

