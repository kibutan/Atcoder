s = input()
n = len(s)//2
#print(n)
cnt = 0
for i in range(n):
  if(s[i] != s[-1-i]):cnt += 1
#  print("i",s[i])
#  print("j",s[-1-i])
print(cnt)
