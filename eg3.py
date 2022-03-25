a=[1,2,3,6,4,1,2]
flag=0
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(a[i])
            c+=1
        else:
            flag+=1
if(flag!=0) and c==0:
    print(-1)
            

