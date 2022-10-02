#!/usr/bin/python

import argparse
import platform
import os

parser = argparse.ArgumentParser(description='ping sweep')
parser.add_argument('network_ip', type=str, help='Input base of ip address')
parser.add_argument('start', type=int, help='starting digit for range')
parser.add_argument('end', type=int, help='ending digit for range')

args=parser.parse_args()

oper = platform.system()

if(oper == "Windows"):
	ping = "ping -n 1 "
else:
	ping = "ping -c 1 "

for ip in range (args.start,args.end+1):
	addr = args.network_ip + "." + str(ip)
	command = ping + addr
	response = os.popen(command)
	list = response.readlines()

	for line in list:
		if(line.count("64 bytes")):
			print(addr)
			break
