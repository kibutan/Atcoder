n = int(input())
a = sorted(list(map(int,input().split())))
ans = -1

odd = [i for i in a if i%2 == 1]
even = [i for i in a if i%2 == 0]

# print(odd)
# print(even)
if(len(even) == 1 and len(odd) == 1 ):
    ans = -1
elif(len(even) == 1 and len(odd) >= 2 or len(even) == 0):
    ans = odd[-1] + odd[-2]
elif(len(even) >= 2 and len(odd) == 1 or len(odd) == 0):
    ans = even[-1] + even[-2]
else:
    ans = max( ans ,( even[-1] + even[-2] ) , (odd[-1] + odd[-2]))

print(ans)
