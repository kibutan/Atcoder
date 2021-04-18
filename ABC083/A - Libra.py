a,b,c,d = list(map(int,input().split()))
if(a + b == c + d):print("Balanced")
elif(a+b > c + d):print("Left")
elif(a+b < c + d):print("Right")
  
