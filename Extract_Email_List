#this code will read the text from the textfile and it will extract all the emails with .com domain and it will print all the emails.


import re
my_file = open("D:\\rand.txt",'r')

while my_file:
    line = my_file.readline()
    result = re.search(r"\w+@\w+.com",line)
    if(result):
        print(result.group())
