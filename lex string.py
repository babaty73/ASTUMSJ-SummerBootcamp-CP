#codeforces problem - 1689A lex strings
t = int(input().strip())

for _ in range(t):
    n, m, k = map(int, input().strip().split())
    
    a = sorted(list(input().strip()))
    b = sorted(list(input().strip()))
    
    c = []
    
    streak_a = 0
    streak_b = 0
    
    while len(a) > 0 and len(b) > 0:
        if (a[0] < b[0] and streak_a < k) or (streak_b == k):
            c.append(a.pop(0))
            streak_a += 1
            streak_b = 0
        else:
            c.append(b.pop(0))
            streak_b += 1
            streak_a = 0
            
    print("".join(c))
