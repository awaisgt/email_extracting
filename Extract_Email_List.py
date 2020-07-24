#this code will read the text from the textfile and it will extract all the emails with .com .fr .de .net .in .pk .it domain and it will print all the emails.


import re
my_list = []
my_file = open("file.txt",'r',encoding="utf8")
line = my_file.readline()
while line:
    line = my_file.readline()
    result = re.search(r"\w+@\w+.(com|fr|de|net|in|pk|it)",line)
    if(result):
        my_list.append(result.group())

for x in my_list:
    print(x)

