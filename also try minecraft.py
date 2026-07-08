#codeforces problem 1709B also try minecraft
n, q = map(int, input().split())
a = list(map(int, input().split()))
forward = [0] * n

for i in range(1, n):
    if a[i] < a[i-1]:
        forward[i] = forward[i-1] + (a[i-1] - a[i])
    else:
        forward[i] = forward[i-1]

backward = [0] * n

for i in range(n - 2, -1, -1):
    if a[i] < a[i+1]:
        backward[i] = backward[i+1] + (a[i+1] - a[i])
    else:
        backward[i] = backward[i+1]

for _ in range(q):
    l, r = map(int, input().split())

    l -= 1
    r -= 1

    if l < r:
        print(forward[r] - forward[l])
    else:
        print(backward[r] - backward[l])
