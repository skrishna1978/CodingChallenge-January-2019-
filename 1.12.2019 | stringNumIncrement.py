#1.12.2019 - shashi
#program that accepts a string and increments the number that is part of it.
#the number has no specific format and can appear however. So an example would be:
# "Member001" that is incremented to "Member002"
#Another example is "hello1" which is incremented to "hello2".
#the only standard is that the number is at the END of the string.

def stringIncrease(s): #function starts here
    if not s: #if string empty
        return "N/A" #return N/A
    
    #else the rest    
    output="" #for final output
    digExtract = "" #for processing the number part of the string
    
    for i in range(5,0,-1): #loop starts at 5, ends at 1, decremented by 1.
        if len(s) > i-1 and s[-i].isdigit():  #check for digits at the end of the string
            digExtract = str(int(s[-i:])+1).zfill(i) #add 1 to the int() portion of the string
            #zfill pads the string's width and helps process values like "0003" without losing 0s.
            output = s[:-i] + digExtract #add the incremented portion to rest of the string
            return output #return the final output back
    #end of loop            
    return s+'1' #this part executed if string has no digits at the end.
    #So "hello" returns "hello1"

#testing diff. kinds of inputs to see how output differ
print(stringIncrease("Member002")) #mixed values with leading 0s (use of zfill())
print(stringIncrease("hello1")) #mixed values withiut leading 0s
print(stringIncrease("justAString")) #no numbers in string
print(stringIncrease("")) #empty string
print(stringIncrease("32")) #only numbers in string
#end of program
