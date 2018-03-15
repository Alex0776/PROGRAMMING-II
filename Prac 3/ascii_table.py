MAX_COLUMNS = 10
MIN_COLUMNS = 2

LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>4}".format(value, chr(value)))


def get_number_in_range(LOWER, UPPER):
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    while number < LOWER or number > UPPER:
        number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
    return number


main()