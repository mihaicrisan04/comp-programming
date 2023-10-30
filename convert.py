
def get_number_from_user_in_base(base: int) -> str:
    while True:
        try:
            number = input(">>>")
            print()

            if number == "":
                print(YELLOW + "Invalid number. Please enter a number" + RESET)
            
            elif number[0] == "-":
                print(YELLOW + "Invalid number. Please enter a positive number" + RESET)

            return number

        except ValueError:
            print(YELLOW + "Invalid number. Please enter a positive number" + RESET)

def get_rapid_base_from_user() -> int:
    while True:
        try:
            base = int(input(">>>"))
            print()

            if base != 2 and base != 4 and base != 8 and base != 16:
                print(YELLOW + "Invalid base. Please enter a number from this list(2, 4, 8, 16)" + RESET)

            else:
                return base

        except ValueError:
            print(YELLOW + "Invalid base. Please enter a number" + RESET)


def rapid_conversion_method(number: str, base: int, new_base: int) -> int:
    """
    Description: This function converts a number from a base to another base using the rapid conversion method

    Parameters:
    number (str): the number to be converted
    base (int): the base of the number
    new_base (int): the new base of the number

    Returns int: the number converted to the new base
    """

    bases = [2, 4, 8, 16]

    bases_big_to_small_dictionary = {
        2: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
        4: ["0", "1", "2", "3", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"],
        8: ["0", "1", "2", "3", "4", "5", "6", "7", "10", "11", "12", "13", "14", "15", "16", "17"],
        16: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B" ,"C", "D", "E", "F"]
    }

    bases_small_to_big_dictionary = {
        42: ["00", "01", "10", "11"],
        82: ["000", "001", "010", "011", "100", "101", "110", "111"],
        162: ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
        84: ["00", "01", "02", "03", "10", "11", "12", "13"],
        164: ["00", "01", "02", "03", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"],
        168: ["00", "01", "02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15", "16", "17"],
        2: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"],
        4: ["0", "1", "2", "3", "10", "11", "12", "13", "20", "21", "22", "23", "30", "31", "32", "33"],
        8: ["0", "1", "2", "3", "4", "5", "6", "7", "10", "11", "12", "13", "14", "15", "16", "17"],
        16: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B" ,"C", "D", "E", "F"]
    }

    result = ""

    if base > new_base:
        for digit in number:
            result += bases_big_to_small_dictionary[new_base][bases_big_to_small_dictionary[base].index(digit)]

    else:
        # conversion from a bigger base to a smaller base
        base_dif = bases.index(new_base) - bases.index(base) + 1
        offset = base_dif - len(number) % base_dif if len(number) % base_dif != 0 else 0

        for i in range(offset):
            number = "0" + number

        index = base + 10 * new_base

        for i in range(0, len(number), base_dif):
            result += bases_small_to_big_dictionary[new_base][bases_small_to_big_dictionary[index].index(number[i:i + base_dif])]

    return result


def rapid_conversion():
    print("Entered the rapid conversion method")

    print("Enter the base(2, 4, 8, 16)")
    base = get_rapid_base_from_user()

    print("Enter the number")
    number = get_number_from_user_in_base(base)

    print("Enter the new base(2, 4, 8, 16)")
    new_base = get_rapid_base_from_user()

    print("The result is: ", end = "")
    print(rapid_conversion_method(number, base, new_base))


rapid_conversion_method("11110001", 2, 4)