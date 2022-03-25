def primeCount(arr, n):
    max_val = max(arr)
    prime = [True] * (max_val+1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= max_val: 
        if prime[p] == True: 
            for i in range(p * 2, max_val+1, p):
                prime[i] = False         
        p += 1
    count = 0
    for i in range(0, n):
        if prime[arr[i]]:
            count += 1
 
    return count
def getPrefixArray(arr, n, pre):
    pre[0] = arr[0]
    for i in range(1, n): 
        pre[i] = pre[i - 1] + arr[i]
arr = [2,4,5,6]
n=len(arr)
pre = [None] * n
getPrefixArray(arr, n, pre)
print(primeCount(pre, n))
