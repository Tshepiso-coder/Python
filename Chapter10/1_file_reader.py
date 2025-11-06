# READING CONTENTS OF A FILE
from pathlib import Path

import math

path =  Path("pi_digits.txt")
contents = path.read_text()
print(contents.rstrip())

# WORKING WITH FILE CONTENTS
lines = contents.splitlines()
for line in lines:
    print(line)
print(lines)    

pi_string = ""
for line in lines:
    pi_string += line.lstrip() # removes the left space from the 2nd and 3rd lines from the file
    
    
print(pi_string)
print(len(pi_string))


path =  Path("pi_ten_million.txt")
contents = path.read_text()

pi_string = contents.splitlines()
print(pi_string[:52])
