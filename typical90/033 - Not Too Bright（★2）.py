h,w = map(int,input().split())
sum = 0
if(h ==1 or w == 1):sum = h*w
else:sum =((h+1)//2)*((w+1)//2)
print(sum)
