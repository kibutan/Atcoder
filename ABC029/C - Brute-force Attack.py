import sys
from itertools import product
input = sys.stdin.readline
n = int(input())
abc = {"a":"a","b":"b","c":"c"}

def solve():
    for i in product(abc,repeat=n):
        print("".join(i))
solve()
