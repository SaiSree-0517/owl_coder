import math as m
n=int(input())
a,b=map(int,input().split())
for i in range(n):
    x,y=map(int,input().split())
    if m.gcd(x,y)==m.gcd(a,b):
        print("yes")
    else:
        print("no")