##適当な関数の最大値か最小値を考える
## 
def f(x):
    return x**2 + 2.3*x + -5

left = -100
right = 100
print(abs(left - right))
while(abs(left - right) > 0.0001 ):
    mid_l = left*(2/3) + right*(1/3)
    mid_r = right*(2/3) + left*(1/3)
    if(f(mid_l) < f(mid_r)):
        right = mid_r
    else:
        left = mid_l
print(right)
print(f(right))
