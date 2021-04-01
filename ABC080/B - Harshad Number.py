def digit(num):
  string = str(num)
  sum = 0
  for i in range(len(string)):
    sum += int(string[i])
  return sum
  
  
  
n = int(input())
if(n % digit(n) == 0):print("Yes")
else:print("No")
