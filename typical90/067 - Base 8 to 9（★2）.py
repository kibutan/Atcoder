def dec2nin(n):
    digit = 0 
    for i in range(22):
        if(n >= 9 ** i):digit += 1
        else:break

    n_nin = 0
    for i in range(digit):
        if(n >= 9**(digit-(i+1))):
            n_nin += n//9**(digit-(i+1)) * (10**(digit-(i+1)))
            n %= 9**(digit-(i+1))
    return n_nin

n_str,k_str = map(str,input().split())
n_oct = int(n_str,8)
k = int(k_str)

for j in range(k):
    n_oct = dec2nin(n_oct)
    if(j == k-1):n_oct = int(str(n_oct).replace("8","5"))
    else:n_oct = int(str(n_oct).replace("8","5"),8)
print(n_oct)
