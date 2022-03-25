a=[int(i) for i in input().split()]
t=int(input())
l=0
h=len(a)-1
c=0
while h>=l:
    m=(l+h)//2
    if a[m]==t:
        print(m)
        break
    elif a[m]>t:
        h=m-1
    else:
        l=m+1
    m=(l+h)//2
