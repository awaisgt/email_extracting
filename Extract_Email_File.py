#This code will read the data from a file and then it will extract emails ending with .com and after that it will store emails to a new file.

import re
my_file = open("myfile.txt",'r') #instead of myfile.txt put your file path
while my_file:
    line = my_file.readline()
    result = re.search(r"\w+@\w+.com",line)
    if(result):
        store_file = open("result.txt",'a') #you can change the file name and file path
        store_file.write(result.group()+"\n")
