#1.22.2019 - shashi
#Program that accepts a sequence of letters and returns the missing letter

def missingLetter(seq):
    alphabetSet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    startingLetter = alphabetSet.index(seq[0]) #index searches for position of first letter in input and returns it
    
    for letter in range(len(seq)): #loop through the length of sequence given
        if not seq[letter] == alphabetSet[startingLetter+letter]: #for each letter check if next letter matches whats in alphabetSet
            return alphabetSet[startingLetter+letter] #if not then return that value back
    #loop ends
    
#testing out function
print(missingLetter(['e', 'f', 'g', 'i', 'j']))
print(missingLetter(['A', 'B', 'C', 'E']))
print(missingLetter(['z', 'A', 'C', 'D']))
#end of program
