#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hex2text(n):
    print(bytearray.fromhex(n).decode())

n = input("Enter the hexadecimal value you want to conver to text: ")

hex2text(n)
