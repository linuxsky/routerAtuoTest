__author__ = 'shiyang'
#encoding:UTF-8

import ConfigParser

import UT_serial


CONFIG_FILE = "config.conf"

def uart_test():
    print "main entry"
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    uart_name = cf.get("serial","SER_NAME")
    uart_batrate = cf.getint("serial","SER_BARATE")
    print uart_name
    print uart_batrate
    UT_serial.Test_serial_main(uart_name,uart_batrate)

if __name__ == '__main__':
    uart_test()
