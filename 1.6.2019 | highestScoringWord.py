#1.6.2019
#Return highest scoring word with a=1, b=2, c=3, ... z=26.
#all input is lower case and valid.

def highestScore(sentence): #function starts here
    words=sentence.split(' ') #split the sentence based on space and make an array
    scoreslist = [] #create list for holding scores for each word
    for word in words: #loop through each word in the sentence
        score = [sum([ord(char) - 96 for char in word])] # critical line : each character of each word's value is loaded and total added via sum()
        scoreslist.append(score) #final score for that word added to scoreslist
        #loop continues until all words are processed.
    return words[scoreslist.index(max(scoreslist))] #max(scoresList[]) returns the highest value which is sent to .index() that pulls out its position
                                                    #words[positon] then is the specific word that has highest score.    

print(highestScore("hakuna matata. what a wonderful phrase!")) 
print(highestScore("wishing everyone a happy new year with a lot of zzzzz"))
