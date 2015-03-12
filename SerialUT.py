__author__ = 'shiyang'
#encoding:UTF-8

import serial

class SerialUT:
    def __init__(self,name,speed):
        self.SerName=name
        self.SerSpeed=speed
    def SerOpen(self):
        try:
            tempSer = serial.Serial( self.SerName, self.SerSpeed ,timeout=2)
            return tempSer.isOpen()
        except:
            return 1;
