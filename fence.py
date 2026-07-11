n, k= map(int, input().split())
h = list(map(int, input().split()))
current = sum(h[:k])
min_sum = current 
min_index = 0
for i in range(1, n-k + 1):
    current =current - h[i - 1] + h[i + k - 1]
    if current  < min_sum:
        min_sum = current 
        min_index = i
print(min_index + 1)