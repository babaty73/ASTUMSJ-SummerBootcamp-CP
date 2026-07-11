def solve():
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input()
        
        first_a = -1
        last_b = -1
        
        # Find the first occurrence of 'A'
        for i in range(n):
            if s[i] == 'A':
                first_a = i
                break
                
        # Find the last occurrence of 'B'
        for i in range(n - 1, -1, -1):
            if s[i] == 'B':
                last_b = i
                break
        
        # If no 'A' exists, no 'B' exists, or first 'A' comes after last 'B'
        if first_a == -1 or last_b == -1 or first_a > last_b:
            print(0)
        else:
            print(last_b - first_a)

# Run the solution
solve()
