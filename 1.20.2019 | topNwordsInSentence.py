#1.20.2019 - Shashi
#Program that accepts a string/sentence and a number N.
#Function should return the the TOP N words occurring in the sentence.

import collections #high performance data type module

def topN_words(text, topNum): #function starts here
    counts = collections.Counter(text.split()) #splits the sentence, implements count numbers as object
    return counts.most_common(topNum)  #counts.most_common built in to return N top words from sentence.
    
#testing function for different strings and N
print(topN_words("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",5))
print(topN_words("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour.",3))
