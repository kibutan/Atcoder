s = [list(input()) for _ in range(8)]
x = ["a","b","c","d","e","f","g","h"]
ans = ""
for i in range(8):
  if("*" in s[i]):
#    print(i,s[i])
    ans = x[s[i].index("*")]+ str(8-i)
print(ans)
