from collections import Counter

n,m = map(int,input().split())
a = Counter(list(input().split()))
b = Counter(list(input().split()))

for key,value in b.items():
    if(not a.get(key)):
        print("No")
        exit()
    elif( a.get(key) < value ):
        # print("No",a.get(key),value,a.get(key) < value  )
        print("No")
        exit()
print("Yes")
