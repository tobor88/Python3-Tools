#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re



h = input("Enter a hexadecimal value to convert to decimal: ")
def main(h):
    dec = int(h, 16);
    print(h,"in Decimal =",str(dec));

main(h)
