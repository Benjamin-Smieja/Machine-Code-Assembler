
def mv(Din):
    Imm = "000"
    imData = isImmediateData(Din[1])

    if( imData ):
        HexToBinary(Din[1])

    else:
        pass

    completeCode = Imm + str(imData) 
    return completeCode


def mvt():
    print("You Called Move Top!!")



def isImmediateData(op):
    return 0 if op[0] == "r" else 1

def HexToBinary(hex):
    nibbles = []
    
    for index, digit in enumerate(hex):
        for i in range(4): nibbles.append(0)
        dig = int(digit)
        for i in range(4):
            nibbles[index*4 + 3-i] = dig//(2**(3-i))
            dig = dig - nibbles[index*4 + 3-i]*(2**(3-i))
        
    
    print(nibbles)