N = int(input())
s = input()
t = ""
 
for i in s:
  t+=i
#  print(t)
#  if("fox" in t):
  if t[-3:] == "fox":
     t = t[:-3:]
#    print(t)
#    print(t)
print(len(t))
