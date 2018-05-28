#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import sys
import time
import serial
import xlsxwriter
import thread
import Queue
"""
VARIAVEIS GLOBAIS (NESTE EXEMPLO)
"""
workbook = xlsxwriter.Workbook('dados.xlsx')
worksheet = workbook.add_worksheet()
global stop

DEVICE='/dev/ttyACM0'
BAUD_RATE='9600'
TIMEOUT='1'
PARITY='N'
STOPBITS='1'
BYTESIZE='8'

def monitora(b,c):
    a = int(input())
    if a  == 1:
        global stop
        stop = 1
    print 'Leu entrada'

def InfoComSerial():
 print '\nObtendo informacoes sobre a comunicacao serial\n'
 # Iniciando conexao serial
 comport = serial.Serial(DEVICE, int(BAUD_RATE), timeout=int(TIMEOUT), bytesize=int(BYTESIZE), stopbits=int(STOPBITS), parity=PARITY)
 # Alem das opcoes rtscts=BOOL, xonxoff=BOOL, e dsrdtr=BOOL
 # Link: http://pyserial.sourceforge.net/pyserial_api.html#constants
 #time.sleep(1.8) # Entre 1.5s a 2s
 #print '\nStatus Porta: %s ' % (comport.isOpen())
 row = 1
 col = 0
 print '\nStatus Porta: %s ' % (comport.isOpen())
 global stop
 stop = 0
 q=Queue.Queue()
 thread.start_new_thread( monitora , (None,None, ))

 while (stop != 1):
    Value = comport.read(5)
    q.put(Value)
    print '\nRetorno da serial: %s' % (Value)
    Value = None
    
 while (q.empty() == False):
    worksheet.write(row, 0, q.get())
    row +=1




 # Fechando conexao serial
 workbook.close()
 comport.close()



""" main """
if __name__ == '__main__':
 InfoComSerial()
