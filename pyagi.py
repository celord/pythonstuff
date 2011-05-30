#!/usr/bin/env python
#
#       pyagi.py
#
#       

import sys

# Read and ignore AGI environment (read until blank line)
env = {}
tests = 0;

# Get a dump of all the environment variables passed to the AGI scr
while 1:
   line = sys.stdin.readline().strip()
   if line == '':
      break
   key,data = line.split(':')
   if key[:4] <> 'agi_':
      #skip input that doesn't begin with agi_
      sys.stderr.write("Did not work!\n");
      sys.stderr.flush()
      continue
   key = key.strip()
   data = data.strip()

   if key <> '':
      env[key] = data
sys.stderr.write("AGI Environment Dump:\n");
sys.stderr.flush()
for key in env.keys():
   sys.stderr.write(" -- %s = %s\n" % (key, env[key]))
   sys.stderr.flush()


def astexec (application, options):
	sys.stderr.write("EXEC %s %s \"\"\n" % (application, options))
	sys.stderr.flush()
	sys.stdout.write("EXEC %s %s \"\"\n" % (application, options))
	sys.stdout.flush()
	result = sys.stdin.readline().strip()
	
def getdata (filename, timeout, max_digits):
   sys.stderr.write("GET DATA %s %d %d\n" % (filename, timeout, max_digits))
   sys.stderr.flush()
   sys.stdout.write("GET DATA %s %d %d\n" % (filename, timeout, max_digits))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1  

def saynumber (params):
	sys.stderr.write("SAY NUMBER %s \"\"\n" % params)
	sys.stderr.flush()
	sys.stdout.write("SAY NUMBER %s \"\"\n" % params)
	sys.stdout.flush()
	result = sys.stdin.readline().strip()

def salpha (params):
	sys.stderr.write("SAY ALPHA %s \"\"\n" % params)
	sys.stderr.flush()
	sys.stdout.write("SAY ALPHA %s \"\"\n" % params)
	sys.stdout.flush()
	result = sys.stdin.readline().strip() 
	
def hangup (params):
	sys.stderr.write("HANGUP %s \"\"\n" % params)
	sys.stderr.flush()
	sys.stdout.write("HANGUP %s \"\"\n" % params)
	sys.stdout.flush()
	result = sys.stdin.readline().strip() 

def getdata (prompt, timelimit, digcount):
   sys.stderr.write("GET DATA %s %d %d\n" % (prompt, timelimit, digcount))
   sys.stderr.flush()
   sys.stdout.write("GET DATA %s %d %d\n" % (prompt, timelimit, digcount))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1

def streamfile (filename, escape_digits):
   sys.stderr.write("STREAM FILE %s %s\n" % (filename, escape_digits))
   sys.stderr.flush()
   sys.stdout.write("STREAM FILE %s %s\n" % (filename, escape_digits))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1    
      
def wfdig (timelimit):
   sys.stderr.write("WAIT FOR DIGIT %s \n" % timelimit)
   sys.stderr.flush()
   sys.stdout.write("WAIT FOR DIGIT %s \n" % timelimit)
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1
      
def getoption (filename, escape_digits, timelimit):
   sys.stderr.write("GET OPTION %s %s %s \n" % (filename, escape_digits, timelimit))
   sys.stderr.flush()
   sys.stdout.write("GET OPTION %s %s %s \n" % (filename, escape_digits, timelimit))
   sys.stdout.flush()
   result = sys.stdin.readline().strip()
   sys.stderr.flush()
   if result:
      return result
   else:
      result = -1
