from decimal import Decimal
n = int(input())
odd = [i for i in range(1,n+1) if i %2 ==1]
print(Decimal(Decimal(len(odd))/Decimal(n)))
