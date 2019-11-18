from core import convert_radix as cR
import re


def check(keys, input):
    if len(input) > 1:
        return "plz! Just type 1 character"
    else:
        strKeys = "["
        for key in keys:
            strKeys += key + ","
        strKeys += "]"
        if re.search(strKeys, input.upper()):
            return input.upper()
        else:
            return "Wrong key!"


def check_radix_converting(*args):
    # check_option(len = 2): [option (A, B, C, D)], [send message if getting error]
    if len(args) == 2:
        response = check(["A", "B", "C", "D"], args[0])
        while len(response) != 1:
            print(response)
            choose = input(args[1])
            response = check(["A", "B", "C", "D"], choose)
        return response
    # check_number(len = 3): [number], [send message if getting error], [option of (A, B, C, D)]
    elif len(args) == 3:
        number = args[0]
        while not cR.check_number(number, args[2]):
            print("[!] Input Error")
            number = input(args[1])
        return number
