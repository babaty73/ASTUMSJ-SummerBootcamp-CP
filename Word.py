#codeforces problem 59A word
word = input()

lower = 0
upper = 0

for ch in word:
    if ch.islower():
        lower += 1
    else:
        upper += 1

if lower >= upper:
    print(word.lower())
else:
    print(word.upper())
