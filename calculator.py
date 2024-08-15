def main():
    x = int(input("What's x? ")) #converts the user's input to an integer and stores it in x
    print("x squared is:", square(x)) #returning the square value of the square function

def square(n):
   return n * n #return the value of n^2
    

main()
########################################################################################################
#ADDITIONAL NOTES
#z = int(x) + int(y)

#INTEGER VALUES
#x = int(input("What's x? "))
#y = int(input("What's y? "))

#FLOATING POINT VALUES
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#ROUNDING
#Round to the nearest integer
#z = round(x + y)

#Adding commas to values -- 1000 to 1,000
#print(f"{z:,}")

#Round to the nearest hundreths place with division
#z = round(x / y, 2)

#Division
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#Divide
#z = x / y

#How many digits should be printed after the decimal
#print(f"{z:.2f}")

#Different ways of calculating with Exponents
#return n ** 2 -- raising to the power of 2
#return pow(n, 2) -- Python function taking two arguments, 1 = number, 2 = exponent