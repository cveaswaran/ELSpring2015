import os
import time
import sqlite3 as db

def readTemp():
	conn = db.connect('temperature.db')
	cur = conn.cursor()

	tempfile = open("/sys/bus/w1/devices/28-000006982acd/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	
	print 'Current temperature is: '+str(tempF)+' F | '+str(tempC)+' C'
	cur.execute('insert into TempData values (\''+currentTime+'\','+str(tempC)+','+str(tempF)+')')
	conn.commit()
	print 'Temperature logged'


readTemp()

