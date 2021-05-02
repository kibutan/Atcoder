import math
from decimal import Decimal
a,b = list(map(int,input().split()))
rt = int(Decimal(math.sqrt(int(str(a)+str(b)))))
if( Decimal(math.sqrt(int(str(a)+str(b)))) == rt ):print("Yes")
else:print("No")
  
