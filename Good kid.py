#Codeforces problem - 1873B good kid
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    min_index = a.index(min(a))
    a[min_index] += 1
    
    product = 1
    for num in a:
        product *= num
        
    print(product)
