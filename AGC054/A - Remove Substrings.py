n = int(input())
s = input()
# print(s)
ans = -1
if(s[0] != s[-1]):
    print(1)
    exit()
else:
    for i in range(n-1):
        if(s[i] != s[0] and s[i+1] !=s[0]):
            print(2)
            exit()            
print(ans)
