def main():
    name = input("What's your name? ")
    hello(name) #calling the function

#Function definition
def hello(to = "World!"):
    print("Hello,", to)

#Calling main function
main()

########################################################################################################
#ADDITIONAL NOTES 
#Remove whitespace
#
#Capitalize user's input
    #name = name.capitalize()
    #name = name.title() 

#Say "Hello" to user
    #print("Hello,", name + "!")

#OVERIDDING THE DEFAULT VALUES FOR print AND sep
    #print("Hello,", name, sep='') #overriding the default value
    #print("Hello,", end="")

#PRINTING QUOTES
#print('Hello, "friend"')

#Ask user for their name
#name = input("What's your name? ").strip().title() 
    #prompts user to add input
    #remove whitespace from str and capitalize user's input

#Split user's name into first and last name
#first, last = name.split(" ")

#Say "Hello" to user
#print(f"Hello, {first}")

#Function definition
#def hello(to = "World!"):
    #print("Hello,", to)

#hello() #no arguments 
#name = input("What's your name? ")
#hello(name) #calling the function