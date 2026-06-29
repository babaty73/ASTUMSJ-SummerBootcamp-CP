# codeforces problem - 2143A all length substraction
t = int(input())
for _ in range(t):
    n = int(input())
    l = 0
    r = n - 1
    sub = 0
    p = list(map(int, input().split()))
    possible = True
    
    while l <= r:
        left_val = p[l] - sub
        right_val = p[r] - sub
        
        if left_val == 1:
            l += 1
        elif right_val == 1:
            r -= 1
        else:
            possible = False
            break
            
        sub += 1
            
    if possible:
        print("YES")
    else:
        print("NO")
