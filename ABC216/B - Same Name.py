n = int(input())
# a,b = list(map(int,input().split()))
s = [list(map(str,input().split())) for i in range(n)]

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if(s[i][0] == s[j][0] and s[i][1] == s[j][1]):
            print("Yes")
            exit()
print("No")
