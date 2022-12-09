### 1. alphabetical order
s = "without,hello,bag,world"
def reorder_str(s):
    """
    Reorder the string alphabetically
    :param s: input str
    :return: ordered str
    """
    l = s.split(',')
    l = sorted(l)
    new_s = ','.join(l)
    return new_s
print(reorder_str(s))


### 2. List of lists
X = 3
Y = 5
big_l = []
for i in range(X):
    small_l = []
    for j in range(Y):
        small_l.append(i*j)
    big_l.append(small_l)
print(big_l)


### 3. list slicing
n = 20
l = []
for i in range(1, n+1):
    l.append(i**2)
print(l[-5:])


### 4 and 5. filter() and map() functions
l = [0,1,2,3,4,5,6,7,8,9,10]
def is_even(x):
    """
    This function checks if the number is even
    :param x: a number (int)
    :return: True/False
    """
    if x % 2 == 0:
        return True
    else:
        return False
def sq(x):
    """
    This function squares the number
    :param x: input number (int)
    :return: squared number
    """
    return x**2
output = map(sq, filter(is_even, l))
for i in output:
    print(i)


### 6. List comprehension
s = '1,2,3,4,5,6,7,8,9'
l = s.split(',')
new_l = [int(item)**2 for item in l if int(item) % 2 == 0]
# new_l = []
# for item in l:
#     if int(item) % 2 == 0:
#         new_l.append(int(item)**2)
print(new_l)




