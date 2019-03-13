#1.7.2019
#Program that accepts a string and returns the first non repeating letter from it. Case insensitive.

def first_non_repeating_letter(string): #function starts here
     sLower = string.lower() #convert original word/sentence into lower case so both cases can be included
     
     for char in string: #loop through each character/letter in the string
        if sLower.count(char.lower()) == 1: #if lower count of this character in this string is only 1/non-repeating
            return char #return that character back
     return "N/A" #if none found then return N/A
  
#test calls 
print(first_non_repeating_letter('Hi there!')) #i
print(first_non_repeating_letter('abracadabra')) #c
print(first_non_repeating_letter('Happy New Year!')) #H
print(first_non_repeating_letter('aAbBcCDd')) #N/A
