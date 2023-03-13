s = input()
ans = [""] * len(s)
for i in range(0,len(s),2):
    ans[i] = s[i+1]
    ans[i+1] = s[i]
print("".join(ans))
