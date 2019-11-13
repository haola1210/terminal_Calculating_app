option_type = {
    "A": ["Binary", 2],
    "B": ["Octal", 8],
    "C": ["Decimal", 10],
    "D": ["Hexadecimal", 16]
}

def decimal_to_other(number, type):
    result = ""
    if type != 16:
        while number != 0:
            result = str(number % type) + result
            number //= type
    else:

        def bigger_than_ten(number):
            if   number == 10: return "A"
            elif number == 11: return "B"
            elif number == 12: return "C"
            elif number == 13: return "D"
            elif number == 14: return "E"
            elif number == 15: return "F"
            else: return str(number)

        while number != 0:
            result = bigger_than_ten(number % type) + result
            number //= type
    return result

def other_to_decimal(number, type):
    result = 0
    if type != 16:
        for i in range(len(number)):
            result += int(number[i])*type**(len(number)-1-i)
    else:

        def bigger_than_ten(number):
            if   number == "A": return 10
            elif number == "B": return 11
            elif number == "C": return 12
            elif number == "D": return 13
            elif number == "E": return 14
            elif number == "F": return 15
            else: return int(number)

        number = number.upper()
        for i in range(len(number)):
            result += bigger_than_ten(number[i])*type**(len(number)-1-i)

    return result

def convert(number, input_type, output_type):
    temp = other_to_decimal(
        number,
        option_type[input_type][1]
    )
    return decimal_to_other(
        temp,
        option_type[output_type][1]
    )