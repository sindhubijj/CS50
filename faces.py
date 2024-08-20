def main():
    #Get user input
    message = input("Please enter your input: ")

    #Call convert message and pass it 
    result = convert(message)

    #Print result
    print(result)

def convert(message):
    #Replace ":)" for a happy emoji
    message1 = message.replace(":)", '🙂')
        #Python's replace function
    
    #Replace ":(" for a sad emoji
    message2 = message1.replace(":(", '🙁')
        #replacing message1 is the result which is being replaced 
    
    #Return string
    return message2

main() #calling main function