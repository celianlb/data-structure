def convert_nb(roman_nb):
    roman_nb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(roman_nb[roman_nb[i]] if roman_nb[roman_nb[i]] >= roman_nb[roman_nb[i + 1]] else -roman_nb[roman_nb[i]] for i in range(len(roman_nb) - 1)) + roman_nb[roman_nb[-1]]

print(convert_nb("MCMXCIV"))

def convert_roman(number):
    number = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    return sum(number[number[i]] if number[number[i]] >= number[number[i + 1]] else -number[number[i]] for i in range(len(number) - 1)) + number[number[-1]]

print(convert_roman(1994))