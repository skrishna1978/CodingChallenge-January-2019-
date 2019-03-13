#1.27.2019 - Shashi
#Accept a string and convert it its opposite case.
#example: "hello world" would become "HELLO WORLD"


def swapCase(string):  #function starts here
	finalString = "" #string to hold final output
    
	for letter in string: #loop through each letter in the original string
    	if letter.isupper(): # if the letter is upper case
        	finalString = finalString + letter.lower()   #add its lower case equivalent to the final output
    	else:   
        	finalString = finalString + letter.upper()  #else do the opposite
    
    
	return finalString #final output will be the swapped cases for each case type.
    
#testing function
print(swapCase("Hello World"))
print(swapCase("hello WORLD"))
print(swapCase("hElLo WoRlD"))
#program ends here
