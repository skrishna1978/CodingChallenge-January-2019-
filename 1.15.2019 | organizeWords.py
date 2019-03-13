#1.15.2019 - Shashi
#Program that accepts a string with a number in each word.
#Output should organize the words according to the number in the words.

def order(sentence):
    print(sentence)
    words = sentence.split() #split up the word based on spaces

    finalSequence = [] #array to hold the final sorted sequence
    finalSequenceWithoutDigit = []  #array to hold final sorted sequence without the original digit in it.
    
    for word in words: #loop through each of the words
        for letter in word: #check each letter in each word
            if letter.isdigit(): #if a digit is found
                finalSequence.append([int(letter), word]) #add a number and the word associated with it
                finalSequenceWithoutDigit.append([int(letter),word.replace(letter,'')])
                #this loops until all words are done.

    
    finalSequence = sorted(finalSequence, key=lambda x : x[0]) #sort the final sequence by first column key
    finalSequenceWithoutDigit = sorted(finalSequenceWithoutDigit, key=lambda x : x[0]) #sort the final sequence by first column key
    
    print(" ".join([x[1] for x in finalSequenceWithoutDigit]))
    return " ".join([x[1] for x in finalSequence]) #join elements in second column [1] with a space and return.


print(order("3brown The1 fo4x qu2ick"))
print("\n")
print(order("world2. hello1 Th3is tes6t. a5"))
