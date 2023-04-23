n = int(input())
s= input()
l = s.index("|")
r = s.rindex("|")
t = s.index("*")
#print(l,r,t)

[print("in") if l < t and t < r else print("out")]
