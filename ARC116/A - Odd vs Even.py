import math
import collections
t = int(input())
case = [int(input()) for i in range(t)]

for i in case:
  if(i % 4 == 0):print("Even")
  elif(i % 2 == 0):print("Same")
  else:print("Odd")
