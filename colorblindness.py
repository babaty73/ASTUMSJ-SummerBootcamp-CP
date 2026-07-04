#codeforces problem - 1722B colorblindness
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    possible = True
    for i in range(n):
        if (a[i] == 'R' and b[i] != 'R') or (b[i] == 'R' and a[i] != 'R'):
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")