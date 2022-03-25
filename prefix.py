def fillPrefixSum(arr, n, prefixSum):
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
arr =[10, 4, 16, 20 ]
n = len(arr)
l=0
r=n
prefixSum = [0 for i in range(n + 1)]
fillPrefixSum(arr, n, prefixSum) 
if l==0 and r==n:
    print(prefixSum[n])
for i in range(n):
    print(prefixSum[i], " ", end ="")
