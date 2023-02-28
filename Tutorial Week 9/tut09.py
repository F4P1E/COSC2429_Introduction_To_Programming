### 1 and 2. Get input from user and write to file
import os

# get input from user
mess = input('input your message: ')
foldername = input('input your folder name: ')
filename = input('input your file name: ')

# create filepath
filepath = foldername + '\\' + filename
# create folder
os.makedirs(foldername, exist_ok=True)
# for MacOS, you might have to create the file in the subfolder as well
# os.makenod(filepath)

# generate 100 lines of the message
mess = (mess + '\n')*100

# open file, please note the differences between 'r', 'w', and 'a'
f = open(filepath, 'w')
# write or append the message to file
f.write(mess)
# you have to close file for this method
f.close()


### 3. read a file, append numbers and write to new file
in_filepath = 'new_folder\\test.txt'

# convert to list, alter the filename, then join str to out_filepath
l = in_filepath.split('\\')
l[-1] = 'new_' + l[-1]
out_filepath = '\\'.join(l)

# open out_filepath to write/append
out_f = open(out_filepath, 'a')

# open in_filepath to read
with open(in_filepath, 'r') as in_f:
    # read all lines into a lis
    lines = in_f.readlines()
    number = 1
    # loop through the list
    for line in lines:
        new_line = str(number) + line
        number += 1
        # write to the new file
        out_f.write(new_line)

# close the output file
out_f.close()


### 4. find missing values
filepath = 'C:\\Users\\v13260\\Downloads\\edited_vietnam.txt'

# open the file approach
with open(filepath, 'r') as f:
    # read all lines into a list
    lines = f.readlines()
    # loop through the list
    for i in range(len(lines)):
        # split each item into sublist
        sublist = lines[i].split(',')
        # loop through the sublist
        for j in range(len(sublist)):
            # check if there is data at the current (i,j)
            if sublist[j] == '':
                print('Missing value at line', i, 'and column', j)

# pandas approach
import pandas as pd

# read the file
df = pd.read_csv(filepath)

# get list of missing values
list_null = df.isnull().stack()[lambda x: x].index.tolist()
print(list_null)

# # fillna with first missing value
print(df.loc[97,'LocID'])
df['LocID'] = df['LocID'].fillna(704).astype(int)
print(df.loc[97,'LocID'])
#
# # fillna with second missing value
print(df.loc[100,'Time'])
df['Time'] = df['Time'].interpolate().astype(int)
print(df.loc[100,'Time'])