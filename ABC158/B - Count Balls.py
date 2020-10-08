N = list(map(int,input().split()))
if(N[1]==0):print(0)
else:print(int(N[0]*N[1]/(N[1]+N[2])) + N[0]%(N[1]+N[2]))
