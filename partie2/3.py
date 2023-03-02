def phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

def phone_number(n):
    return {"France": "+33 {}{}{} {}{}{}-{}{}{}{}".format(*n), "USA": "+1 {}{}{} {}{}{}-{}{}{}{}".format(*n), "Canada": "+1 {}{}{} {}{}{}-{}{}{}{}".format(*n)}

print(phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))