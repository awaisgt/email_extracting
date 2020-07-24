#This code will read the data from a file and then it will extract emails ending with .com and after that it will store emails to a new file.

import re
my_file = open("file.txt",'r')
line = my_file.readline()
while line:
    line = my_file.readline()
    result = re.search(r"\w+@\w+.fr",line)
    if(result):
        store_file = open("result.txt",'a')
        store_file.write(result.group()+"\n")
      

