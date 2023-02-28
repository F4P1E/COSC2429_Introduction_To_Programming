user_input = []
translate = {}
for line in open('eng2pirate.txt'):
    english, pirate = line.split(',')
    translate[english] = pirate

while user_input != "":
    user_input = input("English: ")
    if user_input == "":
        break
    else:
        tempList = []
        for word in user_input.split():
            tempList.append(translate[word])
        A = ("".join(tempList))
        B = (A.replace('\n',' '))
        B = B.rstrip()
        print(B)