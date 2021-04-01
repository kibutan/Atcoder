s = input()
for i in range(len(s)-1,1,-1):
#  print((s[:(i//2)] , s[(i//2):i]))
  if(s[:(i//2)] == s[(i//2):i]):
    print(len(s[:i]))
    exit()
