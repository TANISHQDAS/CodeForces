n = input()
    
lucky_digit_count = 0
for digit in n:
    if digit == '4' or digit == '7':
        lucky_digit_count += 1
        
if lucky_digit_count == 0:
    print("NO")
else:    
    is_lucky_count = True
    lucky_count_str = str(lucky_digit_count) 
    
    for digit_char in lucky_count_str:
        if digit_char != '4' and digit_char != '7':
            is_lucky_count = False
            break
            
    if is_lucky_count:
        print("YES")
    else:
        print("NO")