n = list(map(int,input().split()))
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in n:
  print(alphabet[i-1],end="")
