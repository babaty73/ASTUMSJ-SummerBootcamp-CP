#Codeforces Problem 1972A - Contest Proposal
t = int(input())

for _ in range(t):
    line = input().strip()
    while not line:
        line = input().strip()
    n = int(line)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    operations = 0
    idx = 0  
    for p in range(n):
        if b[p] < a[idx]:
            operations += 1
        else:
            idx += 1
            
    print(operations)
