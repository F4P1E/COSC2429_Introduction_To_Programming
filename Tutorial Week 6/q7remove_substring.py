# shorter solution
print('hello world'.replace('l', ''))
print('hello world hello'.replace('hello', ''))
print('Banananana'.replace('na', ''))


# longer solution (not preferred)
s = 'Banananana'
print(s.replace('na', ''))


# solution 1
def remove_str1(s, substr):
    """
    This function removes all occurences of a substring in a string
    :param s: original string
    :param substr: substring to be removed
    :return: result string
    """
    new_str = ""
    len_str_1 = len(substr)
    len_str_2 = len(s)
    index = 0
    while index != len_str_2:
        if substr == s[index:(index+len_str_1)]:
            index += len_str_1
            continue
        else:
            new_str += s[index]
            index += 1
    return new_str


print(remove_str1(s, 'na'))


# solution 2
def remove_str2(s, substr):
    """
    This function removes all occurences of a substring in a string
    :param s: original string
    :param substr: substring to be removed
    :return: result string
    """
    while True:
        cur_index = s.find(substr)
        if cur_index == -1:
            break
        new_str = s[:cur_index] + s[cur_index+len(substr):]
        s = new_str
    return new_str


print(remove_str2(s, 'na'))
