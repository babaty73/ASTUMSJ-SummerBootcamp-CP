#codeforces problem - 1789B Serval and Inversion Magic
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    
    mismatch_groups = 0
    possible = True
    
    for i in range(n // 2):
        mirror_char = s[n - 1 - i]
        
        if s[i] != mirror_char:
            if mismatch_groups == 2:
                possible = False
                break
            mismatch_groups = 1
        else:
            if mismatch_groups == 1:
                mismatch_groups = 2
                
    if possible:
        print("Yes")
    else:
        print("No")
