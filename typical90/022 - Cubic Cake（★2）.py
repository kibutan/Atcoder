from decimal import Decimal 
import math
a,b,c = map(int,input().split())
 
gcd = math.gcd(a,math.gcd(b,c))
 
# print(gcb)
 
# print(int((a/gcd-1)+(b/gcd-1)+(c/gcd-1)))
print(int(Decimal((a-gcd)+(b-gcd)+(c-gcd))/gcd))
