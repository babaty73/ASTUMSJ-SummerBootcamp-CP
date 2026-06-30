#  codeforces  problem - 2163A  Souvlaki VS. Kalamaki
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    pattern1 = True
    pattern2 = True
    
    for i in range(1, n, 2):
        if i + 1 < n and a[i] != a[i+1]:
            pattern1 = False
    if n > 2 and a[0] != a[2]:
        pattern2 = False
    for i in range(3, n, 2):
        if i + 1 < n and a[i] != a[i+1]:
            pattern2 = False
    if pattern1 or pattern2:
        print("YES")
    else:
        print("NO")
