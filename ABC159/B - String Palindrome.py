import math
S = input()
ans = "No"
center=math.ceil(len(S)/2) #中央の文字数
S_1st = S[0:center-1]
S_2nd = S[center:len(S)]
 
if(S_1st == S_2nd):
  if(S_1st[::-1] == S_1st):
    ans = "Yes"
 
print(ans)
