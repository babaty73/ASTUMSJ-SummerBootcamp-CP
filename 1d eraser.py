# codeforces problem - 1D Eraser 1873D
t = int(input())
for i in range(t):
    n, k = (map(int, input().split()))
    li = input()
    l = 0
    r = n - 1
    op = 0
    while l <= r:
        if li[l] == "B":
            op += 1
            l += k
        else:
            l += 1
    print(op)






















"""op = 0
for i in range(t):
    n, k = (map(int, input().split()))
    li = input()
    if li[i] == "B":
        op += 1
        li[i].pop()
    print(op)"""

