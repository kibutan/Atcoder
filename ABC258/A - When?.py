n = int(input())
print(str(21+(n//60))+":",end="")
print(str(n%60).zfill(2))
