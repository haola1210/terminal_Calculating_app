from supports import verify_input as vI
from core import convert_radix as cR
from core import infix_to_postfix as itp
from core import cal_postfix_to_result as ptr

menu = """ 
\t SUPER CALCULATOR FX6969

--- Choose one option ---

A. Simple expression calculate.
B. Convert to another radix.
C. Calculate the system of equations.
D. Calculate sigma sum of a function.
"""


def choice():
    print(menu, end = "\n")
    choose = input("Your choice => ")
    response = vI.check(["A","B","C","D"], choose)
    while len(response) != 1:
        print(response)
        choose = input("Choice again => ")
        response = vI.check(["A","B","C","D"], choose)
    if(response == "A"):
        express = input("Type your express under this !\n")
        postfix = itp.infix_to_postfix(express)
        result = ptr.Cal(postfix)
        print("result = ", result)
    elif(response == "B"):

        def correct_input(*args):
            # check_option(len = 2): [option (A, B, C, D)], [send message if getting error]
            if len(args) == 2:
                response = vI.check(["A","B","C","D"], args[0])
                while len(response) != 1:
                    print(response)
                    choose = input(args[1])
                    response = vI.check(["A","B","C","D"], choose)
                return response
            # check_number(len = 3): [number], [send message if getting error], [option of (A, B, C, D)]
            elif len(args) == 3:
                number = args[0]
                while not cR.check_number(number, args[2]):
                    print("[!] Input Error")
                    number = input(args[1])
                return number

        template = lambda message: (
            f"\n--- {message} ---\n\n" +
            "A. Binary(2)\n" +
            "B. Octal(8)\n" +
            "C. Decimal(10)\n" +
            "D. Hexadecimal(16)\n\n" +
            "[Type]╼> "
        )

        input_option = correct_input(
            input(template("Type of the input number")),
            "[Type]╼> ",
        ).upper()

        number = correct_input(
            input(
                f"\n[{cR.option_type[input_option][0]}]╼> "
            ),
            f"\n[{cR.option_type[input_option][0]}]╼> ",
            input_option
        )
        output_option = correct_input(
            input(template("Type of the number you want to convert")),
            "[Type]╼> "
        ).upper()
        
        print("\n[Out]╼>",cR.convert(
                number,
                input_option,
                output_option
            )
        )