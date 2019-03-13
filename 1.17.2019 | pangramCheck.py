#1.17.2019 - Shashi
import string #import the string module

def is_pangram(sentence): #function starts here
    if not sentence: #if blank string
        return "N/A"
    sentence = sentence.lower() #convert string to lower case  
    alphabet = "abcdefghijklmnopqrstuvwxyz" #load up all letters in the alphabet
    
    for letter in alphabet: #loop through each letter in the alphabet
        if letter not in sentence: #if any letter from alphabet is not in sentence
            return False #return FALSE and end loop

    return True #if loop completes and reaches here, return TRUE


print(is_pangram("Cwm fjord bank glyphs vext quiz")) #true
print(is_pangram("The quick brown fox jumps over the lazy dog.")) #true since it contains a-z
print(is_pangram("")) #test for empty string
print(is_pangram("hello world")) #false
