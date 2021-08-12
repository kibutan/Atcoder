# n = int(input())
a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]

if(a > 0 and b == 0):print("Gold")
elif(a == 0 and b > 0):print("Silver")
elif(a > 0 and b > 0):print("Alloy")
