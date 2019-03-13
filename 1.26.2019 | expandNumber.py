#1.26.2019 - Shashi
#program that accepts a number in a string and returns the string where each digit is repeated N number of times.
#example: 312 = 333122 (3 repeated 3 times, 1 repeated once, 2 repeated twice)

def expandNumber(num): #function starts here
    
	if not num or int(num)<=0: #if number is empty or <=0
    	return "N/A"	#return N/A
    
	finalOutput = '' #else prepare string var for final output
    
	for digit in num: #for each digit in number
    	finalOutput = finalOutput +  digit*int(digit) #append "digit x (number of times it appears)"
    
    
	return finalOutput #once loop is done return final output back

#testing the function
print(expandNumber("312")) #333122
print(expandNumber("4172")) #44441777777722
print(expandNumber("3241")) #3332244441
print(expandNumber("-3434")) #N/A
print(expandNumber("")) #N/A
#program ends here
