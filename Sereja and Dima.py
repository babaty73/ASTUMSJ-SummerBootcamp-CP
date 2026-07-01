#codeforces problem - 381A sereja and dima
n = int(input())
k = list(map(int, input().split()))

s = 0
d = 0
l = 0 
r = n - 1

for i in range(n):
    if k[l] >= k[r]:
        chosen = k[l]
        l += 1  
    else:
        chosen = k[r]
        r -= 1 
    if i % 2 == 0:
        s += chosen
    else:
        d += chosen
print(s, d)

