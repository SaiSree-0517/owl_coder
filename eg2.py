A=1
B=2
C=3
l=[]
for i in range(A,B+1,C):
    l.append(i)
if B in l:
    print("1")
else:
        print("0")
