# n = int(input())
x,y = list(map(int,input().split(".")))
# print(x,y)
# m = [list(map(int,input().split())) for i in range(n)]

if(0 <= y and y <=2):print(str(x)+"-")
elif(3 <= y and y <=6):print(x)
elif(7 <= y and y <=9):print(str(x)+"+")
