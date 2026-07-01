#codeforces problem - 1791C prepend and append
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = 0 
    r = n -1
    count = 0
    while l <= r:
        if s[l] != s[r]:
            l += 1
            r -= 1
            count += 1
        else:
            break
    print(r-l+1)