s = input()
ans = 0
for index,value in enumerate(s):
  #print(index,value)
  ans += pow(26,len(s)-index-1)*(ord(value) - ord("A")+1)
print(ans)
