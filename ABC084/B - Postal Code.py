a,b = list(map(int,input().split()))
s = input()
ans = "Yes"

for i in range(a):
    if("0" <= s[i] <= "9"):continue
    else:
        print("No")
        exit()
if(s[a] =="-"):ans = "Yes"
else:
    print("No")
    exit()
for j in range(b):
    if("0" <= s[a+1+j] <= "9"):continue
    else:
        print("No")
        exit()
print("Yes")
