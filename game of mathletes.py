#Codeforces Problem 2060C  Game of Mathletes.
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    score = 0
    le = list(map(int, input().split()))
    le.sort()
    left = 0
    right = len(le) - 1
    while left < right:
        current_sum = le[left] + le[right]
        
        if current_sum == k:
            score += 1    
            left += 1       
            right -= 1      
        elif current_sum < k:
            left += 1       
        else:
            right -= 1      

    print(score)