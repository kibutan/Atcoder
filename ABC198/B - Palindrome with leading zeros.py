n = input()
string = []
ans = "Yes"
for i in n:
  if(i != '0'):
    string.append(i)
#print(string)
for j in range(len(string)//2):
#  print(string[j])
  if(int(string[j]) != int(string[-j-1])):
    ans = "No"
    break
  else:continue
print(ans)
  
