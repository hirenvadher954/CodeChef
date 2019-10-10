from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x

t = int(input())

for i in range(t):
    ans = []
    values = list(map(int,input().split()))
    final_values = values[1:]
    gcd_value = find_gcd(final_values)
    
    print(*list(i//gcd_value for i in final_values))
