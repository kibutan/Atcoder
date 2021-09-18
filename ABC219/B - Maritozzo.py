# n = int(input())
# a,b = list(map(int,input().split()))
s = [list(map(str,input().split())) for i in range(3)]
t = input()
for i in range(len(t)):
    print(*s[int(t[i])-1],end="")

