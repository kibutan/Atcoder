#AC
N = int(input())
S = input()
index_i=0
index_j=0
index_k=0

ans = 0
PIN_list =[]

for i in range(10):
  index_i = S[:N-2].find(str(i))
#  print("i"+str(i))
#  print("index_i:"+str(index_i))
  if index_i != -1 :
    for j in range(10):
      index_j = S[index_i+1:N-1].find(str(j))+index_i+1
#      print("j"+str(j))
#      print("index_j:"+str(index_j))
      if (index_j != -1 and index_i < index_j):
#        index_j += index_i + 1
        for k in range(10):
          index_k = S[index_j+1:].find(str(k))+index_j+1
#          print("k"+str(k))
#          print("index_k:"+str(index_k))
          if (index_k != -1 and index_j < index_k):
#            index_k += index_j + 1
#            print("index_i"+ str(index_i) +"index_j"+ str(index_j) +"index_k"+ str(index_k))
#            print(str(i)+str(j)+str(k))
            PIN_list.append(str(i)+str(j)+str(k))
            ans+=1 
print(ans)
#print(PIN_list)
