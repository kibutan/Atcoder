N = int(input())
S = input()
i_list =[]
j_list =[]
k_list =[]
PIN_list = []

for i in range(0,N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if(S[i]+S[j]+S[k] in PIN_list):continue
      else:PIN_list.append(S[i]+S[j]+S[k])
#print(PIN_list)
print(len(PIN_list))
