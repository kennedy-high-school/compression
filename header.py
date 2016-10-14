import array
#format(a[1],"08b"))
global headerEnd;
global headerPointerLength;
headerEnd = 8;
headerPointerLength = 4;
def hex_to_header(hexinput):
    if type(hexinput) == str:
        if hexinput[0:2] == "0x":#remove hex prefix
            hexinput = hexinput[2:]
        if hexinput[len(hexinput) - (headerEnd * 2):] == ("00" * headerEnd): #removes headerEnd
            hexinput = hexinput[0:len(hexinput) - (headerEnd * 2)]
        new_header = []
        for i in range(0,len(hexinput) - 1,(headerPointerLength * 2)):
            new_header.append(int("0x" + hexinput[i:i + (headerPointerLength * 2)],16))
        new_header = array.array('B',new_header)
        return Header(new_header)
    elif type(hexinput) == array.array:
        if (hexinput[len(hexinput) - (headerPointerLength * 2):] == array.array('B',[0,0,0,0,0,0,0,0])):
            hexinput = hexinput[0:len(hexinput) - (headerPointerLength * 2)] #gets rid of header end
        return Header(hexinput)
    else:
        raise NotImplementedError("Invalid type given to create a instance of the Header class.")    
class Header:
    """
    Header class stores pointers to regions of data that is modified in the data region.
    Takes an array as an input to initialize.
    """
    def __init__(self,pointers):
        self.pointers = pointers
    def error_check(self):
        #returns None if no errors found. Returns description otherwise.
        present = []
        for i in range(0,len(self.pointers)):
            if self.pointers[i] in present:
                """
                if printErrors == True:
                    print("".join(("Index " ,str(i) , " in the Header object ", '<%s.%s object at %s>' % (
                    self.__class__.__module__,
                    self.__class__.__name__,
                    hex(id(self))),
                    " is a duplicate pointer of the pointer at index ", str(present.index(self.pointers[i])), " in the Header object. Duplicate pointers are not allowed.")))
                    return 
                else:
                """
                return ("".join(("Index " ,str(i) , " in the Header object ", '<%s.%s object at %s>' % (
                self.__class__.__module__,
                self.__class__.__name__,
                hex(id(self))
                ), " is a duplicate pointer of the pointer at index ", str(present.index(self.pointers[i])), " in the Header object. Duplicate pointers are not allowed.")))
            present.append(self.pointers[i])
        return None
"""
print(hex_to_header("000000020000000800000010000000200000000000000000").pointers)
b = hex_to_header(array.array("B",[2,3,4,6,5,0,0,0,0,0,0,0,0]))
errorCheck = b.error_check()
if errorCheck != None:
    raise IndexError("".join(b.error_check(False)))
"""
