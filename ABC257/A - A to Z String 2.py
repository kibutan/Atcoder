from math import ceil
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,x=map(int,input().split())
print(str[ceil(x/n) -1])
