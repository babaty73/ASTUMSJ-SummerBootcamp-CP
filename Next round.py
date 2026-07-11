n, k = map(int, input().split())
c = list(map(int, input().split()))
cutoff = c[k-1]
count = 0
for i in c:
    if i >= cutoff and i > 0:
        count += 1

print(count)