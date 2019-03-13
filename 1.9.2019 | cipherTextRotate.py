#1.9.2019 - Shashi
#accept a string of text and a key value. cipher the original text based on key value.
#mapping only for lower case letters from a-z.

def cipher(text,key): #function starts here
    arr = "abcdefghijklmnopqrstuwxyz" #lookup variable for all letters.
    text = text.lower() #convert original text to lower
    ctext = "" #variable to hold final output
    for c in text: #loop through every character in string
        #if c is part of alphabet, look up index of c in arr, add key value and mod the whole value by 26 
        #(for high value keys) and look up its equivalent in arr
        if c.isalpha() : ctext += arr[(arr.index(c)+key)%26]  
        else: ctext += c 
        #if c is not in the alphabet, then add it in as is. Example digits, special characters.
    return ctext #return final output back

#testing function with same message but diff. cipher keys.
print(cipher("Hello World 123",3))
print(cipher("Hello World 123",13))
print(cipher("Hello World 123",9))
#end of program
