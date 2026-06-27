#Codeforces problem 2229 A
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    arrs = map(int, input().split())
    arr = sorted(arrs)
    low = arr[0]
    high = arr[-1]
    x = (high - low + 1) // 2
    
    count += x
    
    print(count)
