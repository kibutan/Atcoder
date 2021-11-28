s=input()
t=input()
ans="Yes"
if(s[0]=="." and t[1]=="."):ans="No"
elif(s[1]=="." and t[0]=="."):ans="No"
print(ans)
