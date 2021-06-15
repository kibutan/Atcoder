n = int(input())
a = sorted(list(map(int,input().split())))
# m = [list(map(int,input().split())) for i in range(n)]
 
for i in range(1,n+1):
    if i not in a:
        print("No")
        exit()
print("Yes")
