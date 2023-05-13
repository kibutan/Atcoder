n = input()
s = input()
A_count = s.count("A")
T_count = s.count("T")
if(A_count == T_count):
  print(s[min(s.rfind("A"),s.rfind("T"))])
else:[print("A") if A_count > T_count else print("T")]
