#!/usr/bin/python3

from pwn import *

io = process(["nmap","127.0.0.1"])
output = io.recvall()
print(output.decode())

