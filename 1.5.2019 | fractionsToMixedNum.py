#1.5.2019 - Shashi
#Convert improper fractions to mixed numbers.
#Example: 14/4 = 3 2/4.

def convert(s):
    numbers = s.split("/") #split the string based on / symbol to separate numbers
    numbers = list(map(int, numbers)) #convert string array to integer for the math
    whole = numbers[0]//numbers[1] #whole number is first number/second number
    remainder = (numbers[0]%numbers[1]) #capture remainder of the division
    converted = str(whole) + " " + str(remainder) + "/" + str(numbers[1]) #format final solution
    return converted #return final solution for print
    

print(convert("14/4")) #prints 3 2/4
print(convert("48/7")) #prints 6 6/7
print(convert("9/4")) #prints 2 1/4
#end of program
