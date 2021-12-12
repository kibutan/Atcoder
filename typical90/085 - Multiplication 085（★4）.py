import bisect
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

k = int(input())
div = make_divisors(k)
ans =0
# print(div)
for b_index in range(len(div)):
    ac = k//div[b_index]
    if ac < div[b_index]:continue
    b = div[b_index]
    for a_index in range(bisect.bisect_right(div,b)):
        a =div[a_index]
        if a <= b and k % (a*b) == 0:
            c = k//(b*a)
            if b <= c:
                ans += 1
print(ans)



    
    # print(ac)
