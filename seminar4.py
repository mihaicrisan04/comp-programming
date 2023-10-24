

def generate_list(n):
    # Mihai Crisan
    num_list = []
    # lis = list(range(1,n+1))
    for i in range(1,n+1):
        num_list.append(i)
    return num_list

def binary_search(data, key, left, right):
    # Mihai Crisan
    while left <= right:
        mid = (right + left) // 2
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            right = mid - 1
        elif data[mid] < key:
            left = mid + 1
    return -1

def exponential_search(data, key):
    # Mihai Crisan
    if data[0] == key:
        return 0

    i = 1
    while i < len(data) and data[i] <= key:
        i *= 2

    left = i // 2
    right = min(i, len(data) - 1)
    while left <= right:
        mid = (right + left) // 2
        if data[mid] == key:
            return mid
        elif data[mid] > key:
            right = mid - 1
        elif data[mid] < key:
            left = mid + 1
    return -1



def root_r(number, r, precision):
    if number < 0:
        raise ValueError("Cannot find the square root of a negative number.")

    # Define the initial range [low, high]
    low, high = 0, number

    # Set an initial guess for the root
    guess = (low + high) / 2

    while abs(guess**r - number) > precision:
        if guess**r < number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2

    return guess

print(root_r(2, 10, 0.0001))