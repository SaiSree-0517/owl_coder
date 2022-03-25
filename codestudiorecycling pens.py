n=5
r=10
k=2
c=3
l=1
u=n
while l<=u:
    m=l+u//2
    am=r+(n-m)*k
    if m*c<=am:
        l=m+1
    else:
        u=m-1
print(u)
