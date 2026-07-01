#codeforces problem - 2000B seating in a bus
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    occupied = set()
    occupied.add(a[0])
    possible = True
    for i in range(1, n):
        seat = a[i]
        if (seat - 1 in occupied) or (seat + 1 in occupied):
            occupied.add(seat) 
        else:
            possible = False   
            break  
    if possible:
        print("YES")
    else:
        print("NO")
