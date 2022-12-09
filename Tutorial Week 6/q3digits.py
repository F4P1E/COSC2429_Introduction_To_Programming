def count_digits(n):
    """
    This function counts the number of digits of an integer and return that number, positive integer only
    :param n: an integer
    :return: digit count
    """
    count = 0
    for i in range(len(str(n))):
        count += 1
    return count


# main program
print(count_digits(0))
print(count_digits(10))
print(count_digits(92))
print(count_digits(101))
