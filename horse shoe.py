s1, s2, s3, s4 = map(int, input().split())

buy = 0

if s2 == s1:
    buy += 1

if s3 == s1 or s3 == s2:
    buy += 1

if s4 == s1 or s4 == s2 or s4 == s3:
    buy += 1

print(buy)