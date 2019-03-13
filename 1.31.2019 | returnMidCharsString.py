#1.31.2019 - Shashi
#program that accepts a string and returns the middle character(s).

def extractMid(string):
    
    if not string:
        return "N/A"
    
    strLen = len(string) #to hold the length of the string
    output = ""
    if strLen == 1: #if the string only contains one character
        return string #return the same back
    elif strLen % 2 == 0: #if string contains even number of characters - ex: 6
        output = string[int(strLen/2) - 1] + string[int(strLen/2)] 
        #join middle characters - ex: 3rd and 4th character
        return output #return final output
    else: #if string not 1 and not even count
        return string[int(strLen/2)] 
        #return middle character. So, if length is 5, then mid is 5/2 = 3 which is [2] character.
    

print(extractMid("tested")) #6 characters,so mid should be "st"
print(extractMid("s")) #1 character so returns 's' back
print(extractMid("")) #nothing sent, so N/A returned
print(extractMid("seven")) #5 characters, so 5/2 = 3rd character returned - v
