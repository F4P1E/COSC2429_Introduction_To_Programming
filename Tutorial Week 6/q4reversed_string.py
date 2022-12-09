# shorter solution
print("hello"[::-1])


# longer solution (not preferred)
def reversed_string(s):
    """
    This function returns the reverse of its string parameter
    :param s: a string
    :return: a reverse string
    """
    index = len(s) - 1  # be careful the last index is length -1
    reversed_str = ''
    while index >= 0:
        reversed_str = reversed_str + s[index]
        index = index-1
    return reversed_str


# main program
print(reversed_string("hello"))
