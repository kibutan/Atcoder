n = int(input())
s = input()
cnt = 0
left = 0
right = n-1
for i in range(n-1):
    if(len(set(s[i:i+2])) == 2):
        cnt+=(i-(left-1))*(right-((i+1)-1))
        left = (i+1)
print(cnt)
