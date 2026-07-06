#codeforces problem 41A translation
s = input().strip()
t = input().strip()

if s[::-1] == t:
    print("YES")
else:
    print("NO")