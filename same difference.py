#codeforces problem - 2166A same differences
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    target = s[-1]
    operations = 0
    for i in range(n - 1):
        if s[i] != target:
            operations += 1
            
    print(operations)

