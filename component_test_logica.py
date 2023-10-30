
# def add(first_number: str, second_number: str, base: int) -> str:
#     """
#     Description: This function adds two numbers in a given base

#     Parameters:
#     first_number (str): the first number
#     second_number (str): the second number
#     base (int): the base of the numbers

#     Returns str: the sum of the two numbers
#     """

#     values = "0123456789ABCDEF"

#     result = ""
#     carry = 0

#     while len(first_number) != len(second_number):
#         if len(first_number) > len(second_number):
#             second_number = "0" + second_number

#         else:
#             first_number = "0" + first_number

#     for i in range(len(first_number) - 1, -1, -1):
#         digit1 = values.index(first_number[i])
#         digit2 = values.index(second_number[i])
#         digit = digit1 + digit2 + carry

#         if digit >= base:
#             digit -= base
#             carry = 1

#         else:
#             carry = 0

#         result = values[digit] + result

#     if carry == 1:
#         result = "1" + result

#     return result


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


# def mul(first_number: str, second_number: str, base: int) -> str:
#     """
#     Description: This function multiplies the first number by the second number which is a single digit

#     Parameters:
#     first_number (str): the first number
#     second_number (str): the second number
#     base (int): the base of the numbers

#     Returns str: the product of the two numbers
#     """

#     values = "0123456789ABCDEF"

#     digit2 = values.index(second_number)
#     result = ""
#     carry = 0

#     for i in range(len(first_number) - 1, -1, -1):
#         digit1 = values.index(first_number[i])
#         digit = digit1 * digit2 + carry

#         if digit >= base:
#             carry = digit // base
#             digit %= base

#         else:
#             carry = 0

#         result = values[digit] + result

#     if carry != 0:
#         result = values[carry] + result

#     return result

# print(mul("AA", "2", 16))
# print(mul("2", "2", 16))
# print(mul("111", "1", 2))


def div(first_number: str, second_number: str, base: int) -> str:
    """
    Description: This function divides two numbers in a given base

    Parameters:
    first_number (str): the first number
    second_number (str): the second number
    base (int): the base of the numbers

    Returns str: the quotient of the two numbers
    """
    pass