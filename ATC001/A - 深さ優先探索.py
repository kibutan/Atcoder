import sys
sys.setrecursionlimit(10**6)
 
def search(y,x):
    global c
    global arrive
    # print(c[y][x])
    if(0> x or x >= w or 0 > y or y >= h):return
    if(c[y][x] == "#"):return
    if(arrive[y][x]):return
    if(c[y][x] == "g"):
        print("Yes")
        exit()
    arrive[y][x] = True
 
    search(y+1,x)
    search(y,x+1)
    search(y-1,x)
    search(y,x-1)
 
def return_index(l,s,default=False):
    return True if s in l else default
 
h,w = map(int,input().split())
# c = [list(map(str,input().split())) for i in range(h)]
c = [list(input()) for i in range(h)]
arrive=[[False for _ in range(w)] for _ in range(h)]
# print(arrive)
 
for i in range(h):
    # print(c[i],return_index(c[i],"s"))
    search(i,c[i].index("s")) if return_index(c[i],"s") else None
    # if result:
    #     print("Yes")
    #     exit()
print("No")
