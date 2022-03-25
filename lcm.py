import math as m
a,b=map(int,input().split())
l=(a*b)//(m.gcd(a,b))
print(l)