__author__ = 'shiyang'
#encoding:UTF-8

import ConfigParser

#import SerialUT   使用这个时需要加上模块的限定，否则报错 例如: SerialUT.SerialUI(0.0)
from SerialUT import *

CONFIG_FILE = "config.conf"

def uart_test():
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    uart_name = cf.get("serial","SER_NAME")
    uart_batrate = cf.getint("serial","SER_BARATE")
    ret = SerialUT(uart_name,uart_batrate).SerOpen()
    return ret

if __name__ == '__main__':
    print("1--- test uart port")
    ret = uart_test()
    assert(ret == 0)
    print("finish test uart")

    print("======  auto test done  =======")
