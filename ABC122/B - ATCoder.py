import re
S = input()
length = 0
ans = 0
t = ""
for i in S:
  t += i
#  print(t)
  if(re.findall('A|G|T|C',t[-1])):length += 1
  else: 
#    print("t is not ACTG:" + str(t[-1]))
    t = ""
    ans = max(ans,length,len(t))
    length=0
#    print(ans)
print(max(ans,length))
