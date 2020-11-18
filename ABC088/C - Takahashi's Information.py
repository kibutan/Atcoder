c = [list(map(int,input().split())) for _ in range(3)]
# c_{1,1}=a_1+b_1なるa_1をインクリメントとしてほかが成り立つか
ans = "No"
for i in range(101):
  b_1 = c[0][0]-i
  b_2 = c[0][1]-i
  b_3 = c[0][2]-i
  a_2 = c[1][0]-b_1
  a_3 = c[2][0]-b_1
  #print("B1: "+str(b_1)+", B2:"+str(b_2)+", B3:"+str(b_3))
  #print("A2:"+str(a_2)+", A3:"+str(a_3))
  if(a_2+b_2 == c[1][1] and a_2+b_3 == c[1][2] and a_3+b_2 == c[2][1] and a_3+b_3 == c[2][2]):
    ans = "Yes"
print(ans)
