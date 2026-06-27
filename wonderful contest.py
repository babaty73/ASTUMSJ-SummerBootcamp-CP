#codeforces problem - 2222A awonderful contest
t = int(input())
for i in range(t):
    a = int(input())
    arr=list(map(int, input().split()))
    if max(arr)== 100:
        print("Yes")
    else:
        print("No")
