N = int(input())
s = input()
#print(s.replace("fox",""))
while("fox" in s):
  s = s.replace("fox","")
print(len(s))
