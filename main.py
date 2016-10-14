#imports
import math
import random
import hashlib
#import reduced
#import extended
import header
import stack
global full_file;
full_file = []
new_header = header.hex_to_header("0x0000000800000008000000200000000000000000")
print(new_header.error_check())
new_stack = new_stack = stack.hex_to_stack("00000002015000000004800000FF0000000220AC0000000000000000")
new_stack.items[0][1] = 0xFFFF
print(new_stack.error_check())
exit()
my_file = input("Enter file name: ")
bytes_read = open(my_file, "rb").read()
for b in bytes_read: #reads the bytes of the file and places them in a list
    full_file.append(b)
afile.close()
