__author__ = 'shiyang'
#encoding:UTF-8

import serial

def Test_serial_main(name,speed):
    ser = serial.Serial(name,speed,timeout=2)
    return ser.isOpen()