n,k=list(map(int,input().split()))
s= list(input())
ans = []
passed = 0
for i in s:
  if i == "o" and passed < k:
    passed += 1
    ans.append("o")
  else:
    ans.append("x")
print(("").join(ans))
