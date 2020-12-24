"""
WAP  to accept the name of a text file. Pass it as parameter to the function countNO() that returns the total number of
no. present in the file.
Eg. Input: There were no notations to be jotted.
    Output: 2
"""


def count_no(file_name):
    f = open(f'{file_name}', 'r')
    s = f.read()
    f.close()
    l = len(s)
    c = 0
    i = 0
    while i < l:
        ss = s[i:i + 2]
        if ss == 'no':
            c += 1
        i += 1
    return c


file_name = input('Enter file name with file.extension: ')
c = count_no(file_name)
print('Total no. of "no": ', c)
