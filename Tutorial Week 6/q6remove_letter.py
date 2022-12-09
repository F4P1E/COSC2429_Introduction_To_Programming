# shorter solution
print('Hello'.replace('l', ''))
print('radar'.replace('b', ''))
print('Radar'.replace('R', '').replace("r", ''))


# longer solution (not preferred)
def remove_letter(s, c):
    """
    This function removes all occurrences of a given letter (regardless of upper/lower case difference) from a string
    :param s: the full string
    :param l: parts of the string to be removed
    :return: the result string
    """
    new_string = ''
    for char in s:
        if char.lower() != c.lower():  # or you can write if char != c.lower() and char != c.upper():
            new_string = new_string + char
        # no need for else, as we would do nothing
    return new_string


# main program
print(remove_letter('Hello', 'l'))
print(remove_letter('radar', 'b'))
print(remove_letter('Radar', 'R'))
