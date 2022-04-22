#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getopt
import sys
import re
import argparse


usage="""Syntax: hex2num [-h] -v 
OsbornePro hex2num v1.1 ( https://osbornepro.com )

    DESCRIPTION: hex2num is a tool created to quickly convert hex values to numbers

    USAGE: hex2num -v <hex value to convert> 
    
    OPTIONS:
    -h : Displays the help information for the command.
    -v : Set the hex value to convert to a number 
        
    EXAMPLES:
    hex2num -v FF
    # This example translates FF to 255
          
    cat /tmp/hex.lst | hex2num -v 
    # This example converts a list of hex values to their number
"""
argumentList = sys.argv[1:]
options = "hv:"
long_options = ["help","value"]
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--value", help = "Enter the hex value you want to convert to a number")
args = parser.parse_args()

if args.value:
    h = args.value
    dec = int(h, 16);
    print(h,"in Decimal =",str(dec));

else:
    print(str(usage))
