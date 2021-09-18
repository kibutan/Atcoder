x = int(input())
# a,b = list(map(int,input().split()))
# m = [list(map(int,input().split())) for i in range(n)]
 
if( 0 <= x and x < 40):print(40-x)
elif( 40 <= x and x < 70):print(70-x)
elif( 70 <= x and x < 90):print(90-x)
elif( 90 <= x and x <= 100):print("expert")
