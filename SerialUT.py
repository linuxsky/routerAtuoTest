__author__ = 'shiyang'
#encoding:UTF-8

import serial

class SerialUT:
    def __init__(self,name,speed):
        self.SerName=name
        self.SerSpeed=speed
        self.com=None
    def SerOpen(self):
        try:
            tempSer = serial.Serial( self.SerName, self.SerSpeed ,timeout=2)
            status = tempSer.isOpen()
            if (status == True):
                self.com=tempSer
                return True
            return False
        except:
            return False;
    def SerClose(self):
        if(self.com != None):
            try:
                self.com.close();
            except:
                print("Close uart failed")
        return
    

