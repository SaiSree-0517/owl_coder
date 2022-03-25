nums1=[int(i) for i in input().split()]
nums2=[int(i) for i in input().split()]
l=[]
for i in nums1:
    for j in nums2:
        if i==j:
            l.append(i)
print(l)
