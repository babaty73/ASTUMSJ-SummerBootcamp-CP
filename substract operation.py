#codeforces problem - 1656B subtract operation
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    seen = set(a)
    possible = False
    for i in a:
        if(i + k) in seen:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")