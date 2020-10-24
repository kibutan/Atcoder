import math
N = int(input())
M = 0
A = "-1"
B = ""
for i in range(1,int(math.log(N,5)+1)):
    M = N - 5**i
#    print("i:"+str(i))
    if(M > 0):
      for j in range(1,int(math.log(M,3)+2)):
#        if(j > 35):
#          print("j:"+str(j))
        if((M - 3**j)==0):
          B = " " + str(i)
          A = str(j)
          break
print(str(A)+str(B))
