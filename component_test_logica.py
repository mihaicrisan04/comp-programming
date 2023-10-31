
def add(first_number: str, second_number: str, base: int) -> str:
    """
    Description: This function adds two numbers in a given base

    Parameters:
    first_number (str): the first number
    second_number (str): the second number
    base (int): the base of the numbers

    Returns str: the sum of the two numbers
    """

    values = "0123456789ABCDEF"

    result = ""
    carry = 0

    while len(first_number) != len(second_number):
        if len(first_number) > len(second_number):
            second_number = "0" + second_number

        else:
            first_number = "0" + first_number

    for i in range(len(first_number) - 1, -1, -1):
        digit1 = values.index(first_number[i])
        digit2 = values.index(second_number[i])
        digit = digit1 + digit2 + carry

        if digit >= base:
            digit -= base
            carry = 1

        else:
            carry = 0

        result = values[digit] + result

    if carry == 1:
        result = "1" + result

    return result


# print(add("AA", "1", 16))



# def sub(first_number: str, second_number: str, base: int) -> str:
#     """
#     Description: This function substracts two numbers in a given base

#     Parameters: 
#     first_number (str): the first number
#     second_number (str): the second number
#     base (int): the base of the numbers

#     Returns str: the difference of the two numbers
#     """

#     values = "0123456789ABCDEF"

#     result = ""
#     borrow = 0

#     while len(first_number) != len(second_number):
#         if len(first_number) > len(second_number):
#             second_number = "0" + second_number

#         else:
#             first_number = "0" + first_number

#     for i in range(len(first_number) - 1, -1, -1):
#         digit1 = values.index(first_number[i])
#         digit2 = values.index(second_number[i])
#         digit = digit1 - digit2 - borrow

#         if digit < 0:
#             digit += base
#             borrow = 1

#         else:
#             borrow = 0

#         result = values[digit] + result

#     return result


# print(sub("AA", "1", 16))
# print(sub("1", "AA", 16))
# print(sub("1", "1", 16))
# print(sub("1", "2", 16))
# print(sub("2", "1", 16))
# print(sub("101011", "11", 2))


def mul(first_number: str, second_number: str, base: int) -> str:
    """
    Description: This function multiplies the first number by the second number which is a single digit

    Parameters:
    first_number (str): the first number
    second_number (str): the second number
    base (int): the base of the numbers

    Returns str: the product of the two numbers
    """

    values = "0123456789ABCDEF"

    digit2 = values.index(second_number)
    result = ""
    carry = 0

    for i in range(len(first_number) - 1, -1, -1):
        digit1 = values.index(first_number[i])
        digit = digit1 * digit2 + carry

        if digit >= base:
            carry = digit // base
            digit %= base

        else:
            carry = 0

        result = values[digit] + result

    if carry != 0:
        result = values[carry] + result

    return result

# print(mul("AA", "2", 16))
# print(mul("2", "2", 16))
# print(mul("111", "1", 2))


# def div(first_number: str, second_number: str, base: int) -> (str, str):
#     """
#     Description: This function divides two numbers in a given base

#     Parameters:
#     first_number (str): the first number
#     second_number (str): the second number that is a single digit
#     base (int): the base of the numbers

#     Returns (str, str): the quotient and the remainder of the two numbers
#     """
    
#     # G is added for the successive divisions method as a placeholder for 16
#     values = "0123456789ABCDEFG"

#     quotient = ""
#     remainder = 0

#     for i in range(len(first_number)):
#         digit = values.index(first_number[i])
#         d = remainder * 10 + digit
#         digit = d // values.index(second_number)
#         remainder = d % values.index(second_number)
#         quotient += values[digit]
    
#     quotient = quotient.lstrip("0")
#     remainder = values[remainder]

#     return quotient, remainder




# print(div("101011", "1", 2))
# print(div("AA", "2", 16))
# print(div("999", "3", 10))
# print(div("88", "3", 16))
# print(div("FFFF", "2", 16))


# def successive_divisions_method(number: str, base: int, new_base: int) -> str:
#     """
#     Description: This function converts a number from a base to another base using the successive divisions method

#     Parameters:
#     number (str): the number to be converted
#     base (int): the base of the number
#     new_base (int): the new base of the number

#     Returns str: the number converted to the new base
#     """
    
#     values = "0123456789ABCDEFG"

#     result = ""

#     while len(number) != 0:
#         number, remainder = div(number, values[new_base], base)
#         result = remainder + result

#     return result


# print(successive_divisions_method("2653", 10, 16))


def substitution_method(number: str, base: int, new_base: int) -> int:
    """
    Description: This function converts a number from a base to another base using the substitution method

    Parameters:
    number (int): the number to be converted
    base (int): the base of the number
    new_base (int): the new base of the number

    Returns int: the number converted to the new base
    TODO Check if this is the substitution method?
    """
    # G is used ad a placehoolder for the value 16
    values = "0123456789ABCDEFG"

    result = ""

    if base < new_base:
        # conversion from a smaller base to a bigger base
        number = number[::-1] # reverse the number
        x = "1"
        for digit in number:
            result = add(result, mul(digit, x, new_base), new_base)
            x = mul(x, values[new_base], new_base) # x = x * new_base


    return result

print(substitution_method("354", 6, 8))
print(substitution_method("11011", 2, 4))

