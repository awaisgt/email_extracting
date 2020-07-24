#this code will read the text from the textfile and it will extract all the emails with .com domain and it will print all the emails.


import re
my_list = []
my_file = open("D:\\rand.txt",'r')
line = my_file.readline()
while line:
    line = my_file.readline()
    result = re.search(r"\w+@\w+.fr",line)
    if(result):
        my_list.append(result.group())

for x in my_list:
    print(x)

