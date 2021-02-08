X = int(input())
balance = 100
year = 0
while(balance < X):
  balance += balance//100
  year += 1
print(year)
