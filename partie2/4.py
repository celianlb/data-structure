def camel_case(text):
    return text.title().replace("_", "").replace("-", "")

print(camel_case("Le-roi-des-Rats"))