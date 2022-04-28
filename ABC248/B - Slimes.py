a,b,k = map(int,input().split())
# print(a)
for i in range(31):
    if(a >= b):
        print(i)
        exit()
    a = a*k
