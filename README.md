# Layout:
# Stack then Header then Data
# Header:
# List of pointers to instructions in data
# Each pointer is 32 bits in length. One after another.
# headerEnd = 0x00000000 00000000
# headerEnd specifies the end of the header.
# stackEnd = 0x00000000 00000000
# stackEnd specifies the end of the stack.
# Instruction Set Specifications
# Byte 1
#  00000000
#  1 = Expanded instructions
#  0 = Reduced instructions
# Reduced Instructions:
# 16 bit
#  00000000 00000000
#  0 = Reduced Instrucions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Commented out comments:
#   1111 = Instruction Type
#       111 stack pointer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   111 = Instruction Type
#      1111 = Stack Index/Arg1
#           11111111 = Arg2(other args)
##############################
# Reduced Instructions Set:
#  Instruction Type =  000
#  Repeat Instruction
#  Duplicates Stack Index to be a full byte, than repeats it arg2 times in the instructions place.
#  Example:
#  0b00001111 00010000
#  Produces 0xFFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF
#-----------------------------
#  Instruction type = 001
#  Repeat from Stack Instruction
#  Duplicates the object at the index in the stack arg2 times in the instructions place.
#  Example:
#  Stack[2] = 0b11001100111100001010101000000000 = 0xCCF0AA00
#  0b00010010 00000100
#  Produces 0xCCF0AA00 CCF0AA00 CCF0AA00 CCF0AA00
#------------------------------
#  Instruction type = 010
#  Repeat Reverse from Stack Instruction
#  Duplicates the object at the index in the stack arg2 times in the instructions place, but reverses the bits on every iteration.
#  Example:
#  Stack[3] = 0b1100111100110000 = 0xCF30
#  0b0010011 00001000
#  Produces 0xCF3003FC CF3003FC CF3003FC CF3003FC


Automatic Compressor:
  Goal: Determine best compression instructions to use.
  How: Iterate through the file, testing compression instructions.
  Levels: Different levels of automation/compression can be used for different compression times. Higher levels tend to result in better compressed files, but slower compression.