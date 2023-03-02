def decimal_to_7seg(decimal):
    digits_7seg = {'0': '_|_|_', '1': ' | | ', '2': '_  _|','3': '_  _|', '4': ' |_| ', '5': '_|_  ', '6': '_|_  ', '7': '_  | ', '8': '_|_|_', '9': '_|_|_',}
    
    result = ""
    for digit in decimal:
        result += digits_7seg[digit] + " "

    return result

