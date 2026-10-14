def solve():
    n = int(input())
    percentages = list(map(int, input().split()))
    
    total_percentage = sum(percentages)
    average_percentage = total_percentage / n
    
    print(average_percentage)
 
solve()