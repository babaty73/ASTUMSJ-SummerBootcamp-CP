#codeforces problem -2192A string rotation game
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    blocks = 1
    has_duplicates = False
    for i in range(1, n):
        if s[i] != s[i-1]:
            blocks += 1
        else:
            has_duplicates = True
    if has_duplicates and s[0] != s[-1]:
        blocks += 1
        
    print(blocks)

