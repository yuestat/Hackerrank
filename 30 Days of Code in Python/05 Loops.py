#!/bin/python3

import sys

n = int(input().strip())

i = 1
while (i >=1 and i <= 10):
   result = n * i
   print (n, 'x', i, '=', result)
   i = i+1
