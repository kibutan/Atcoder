s = input()
t = input()
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

cnt= 0
if s == t: 
    print("Yes")
    exit()
index=[]
for i in range(len(s)):
    if(s[i] != t[i]):
        cnt+=1
        index.append(i)

if(cnt == 2):
    if(abs(index[0] - index[1]) == 1):
        if(s[index[0]] == t[index[1]] and s[index[1]] == t[index[0]]):
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()
else:print("No")
