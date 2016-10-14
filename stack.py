global stackEnd;
global stackDataLength;
stackEnd = 8;
stackDataLength = 4;
class Stack:
    def __init__(self,items):
        self.items = items
        #items = [[itemSize, item], [itemSize, ...] ...]
    def error_check(self):
        for i in range(0,len(self.items)):
            #returns error message if error encountered, otherwise returns 
            if (self.items[i][0] * 8) < self.items[i][1].bit_length():
                return("".join(("Invalid object length in stack object " ,
                    '<%s.%s object at %s>' % (
                    self.__class__.__module__,
                    self.__class__.__name__,
                    hex(id(self))),
                    " at index " , str(i) ,
                    ". Length given is " ,
                    str(self.items[i][0]),
                    " bytes. Length of item is ",
                    str((self.items[i][1].bit_length() + (self.items[i][1].bit_length() % 8)) // 8),
                    " bytes.")))
        return None
def hex_to_stack(hexinput):
    if type(hexinput) == str:
        newStack = []
        index = 0
        while 1:
            dataLength = int("0x" + hexinput[index:index + (stackDataLength * 2)],16)
            newStack.append([int("0x" + hexinput[index:index + (stackDataLength * 2)],16),int("0x" + hexinput[index + (stackDataLength * 2):index + (stackDataLength * 2) + (2 * dataLength)],16)])
            index += (dataLength * 2) + (stackDataLength * 2)
            if hexinput[index:index + (stackEnd * 2)] == "00" * stackEnd:
                break
        return Stack(newStack)
    else:
        raise NotImplementedError("Invalid type given to create a instance of the Stack class.")

