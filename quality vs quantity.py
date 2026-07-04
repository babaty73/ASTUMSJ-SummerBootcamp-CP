#codeforces problem - 1646B Quality vs Quantity
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    blue_sum = a[0] + a[1]
    red_sum = a[-1]

    blue = 2
    red = 1

    left = 2
    right = n - 2

    ok = False

    while left <= right:
        if red_sum > blue_sum and red < blue:
            ok = True
            break

        blue_sum += a[left]
        blue += 1
        left += 1

        red_sum += a[right]
        red += 1
        right -= 1

    if red_sum > blue_sum and red < blue:
        ok = True

    print("YES" if ok else "NO")