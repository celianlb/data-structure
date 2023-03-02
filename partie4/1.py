def conway_sequence(n):
    if n == 1:
        return "11"

    term = conway_sequence(n-1)

    count = 1
    current_digit = term[0]
    result = ""
    
    for digit in term[1:]:
        if digit != current_digit:
            result += str(count) + current_digit
            count = 1
            current_digit = digit
        else:
            count += 1

    result += str(count) + current_digit
    
    return result

print(conway_sequence(15))




