import commands
def hello(apple):
    print("OMG IT WORKEDD",apple)

#Take user input and split into different parts of instruction
done = False
while(not done): 
    instruct = input("Processor Instruction:")
    parsed = instruct.strip().split(' ')
    
    #Search for command in commands module
    try:
        method_to_Call = getattr(commands,parsed[0])
    except:
        print("invalid command")
        continue

    #Calls the command 
    method_to_Call(parsed[1:])
    done = 1

