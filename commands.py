
#Move Data from second register/Data into first register
def mv(Din):
    #mv -> 000
    Imm = "000"
    #Checks if instruction is between two registers or immediate data and register
    imData = isImmediateData(Din[1])

    #Calculates primary Register address(3 bits)
    rX = DecToBinary(Din[0][1])

    #If immediate data convert hex data into 9 bits
    if( imData ):
        HexToBinary(Din[1])

    else:
        #Calculate address of secondary register (3bits)
        pass
        #Pad the beggining of the command with 6 zeros
        pass
        rY = "000000110"

    completeCode = Imm + str(imData) +rX + rY
    return completeCode


def mvt():
    print("You Called Move Top!!")


#Checks if the command uses two registers or a register and immediate data from the instruction signal
def isImmediateData(op):
    return 0 if op[0] == "r" else 1

#Takes in a hexadecimal number and returns the binary number as a string
def HexToBinary(hex):
    nibbles = []
    
    #Interate through each Hex digit and covert to nibble
    for index, digit in enumerate(hex):
        print("WORKING ON DIGIT",digit)
        #Prep the MSB for new Digit
        for i in range(4): nibbles.insert(0,0)

        dig = int(digit)
        #Convert Digit to 4 bits by dividing by each column and flooring
        for i in range(4):
            print("DIG IS CURRENTLY:",dig)
            nibbles[3-i] = dig//(2**(3-i))
            dig = dig - nibbles[3-i]*(2**(3-i))
        
    
    nibbles.reverse()
    output = "".join(map(str,nibbles))
    print(nibbles)
    print(output)

#Incomplete Function
def DecToBinary(dec):
    if(False):
        nibbles = []
        
        for index, digit in enumerate(hex):
            for i in range(4): nibbles.append(0)
            dig = int(digit)
            for i in range(4):
                nibbles[index*4 + 3-i] = dig//(2**(3-i))
                dig = dig - nibbles[index*4 + 3-i]*(2**(3-i))
        
    
    return("001")