__author__ = 'shiyang'
#encoding:UTF-8

import os

import ConfigParser
#import SerialUT   使用这个时需要加上模块的限定，否则报错 例如: SerialUT.SerialUI(0.0)
from SerialUT import *
from scapy.all import *
from SshUT import *

CONFIG_FILE = "config.conf"

def uart_test():
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    uart_name = cf.get("serial","SER_NAME")
    uart_batrate = cf.getint("serial","SER_BARATE")
    uart = SerialUT(uart_name,int(uart_batrate))
    ret = uart.SerOpen()
    if(ret == True):
        uart.SerClose()
    assert(ret == True)

def arp_icmp_ping():
    ret =0
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    gwip = cf.get("lan","SERIP")

    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=gwip),timeout=2)
    ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )
    for p in ans : gw_mac = p[1][Ether].src
    #assert(len(ans) != 0)

    ans,unans=sr(IP(dst=gwip)/ICMP(),timeout=2)
    ans.summary(lambda (s,r): r.sprintf("%IP.src% is alive") )
    #for p in ans : print p[1][IP].src
    assert(len(ans) != 0)

def scan_gw_port(port):
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    gwip = cf.get("lan","SERIP")

    res,unans = sr( IP(dst=gwip)/TCP(flags="S", dport=port) )
    for p in res :
        if(p[1][TCP].flags == 18):
            return 0
    return 1

def ssh_connet(ip,username,passwd):
    cmd = ['ps']
    return ssh2(ip,username,passwd,cmd)

if __name__ == '__main__':
    print("\033[41;36m|== test uart port ==|\033[0m")
    uart_test()

    print("\033[41;36m|== test arp and icmp gateway ==|\033[0m")
    arp_icmp_ping()

    print("\033[41;36m|== test ssh(tcp port 22) ==|\033[0m")
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    sship = cf.get("lan","SERIP")
    passwd = cf.get("ssh","PASSWD")
    username = cf.get("ssh","USERNAME")
    sshport = cf.get("ssh","SSHPORT")
    ret = scan_gw_port(int(sshport))
    if(ret == 0):
        ret = ssh_connet(sship,username,passwd)
    assert(ret == 0)

    print("\033[41;36m|== router auto test done ==|\033[0m")
