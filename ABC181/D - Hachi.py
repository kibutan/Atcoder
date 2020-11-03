from collections import Counter
 
n = input()
 
if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
cnt = Counter(n)
 
for i in range(104, 1000, 8): #解説はなぜ112から始まっているのか?
    if not Counter(str(i)) - cnt:
      print("Yes")
      exit()
print("No")
