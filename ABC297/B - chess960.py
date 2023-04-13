s=input()
if(s.find("B")%2 != s.rfind("B")%2):
  if(s.find("R") < s.find("K") and s.find("K") < s.rfind("R")  ):
    print("Yes")
    exit()
print("No")
