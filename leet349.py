nums1=[int(i) for i in input().split()]
nums2=[int(i) for i in input().split()]
a=list(set(nums1))
b=list(set(nums2))
l=[]
for i in a:
    for j in b:
        if i==j:
            l.append(i)
print(l)
