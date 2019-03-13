#1.14.2019 - shashi
#Program to generate a random password based on number of characters requested.
import random
import string
#import built in libraries to use specific functions

def genpwd(length): #function starts here
    password = ""  #to hold final value
    count = 0      #to keep track of length required
    
    if length<=0:   #to handle error values
        return "N/A" 

    while count != length: #as long count does not become equal to requested length
        dig = [random.choice(string.digits)] #get a randomly selected digit
        upper = [random.choice(string.ascii_uppercase)]  #get a randomly selected uppercase letter
        lower = [random.choice(string.ascii_lowercase)] #get a randomly selected lowercase letter
        spec = [random.choice(string.punctuation)] #get a randomly selected symbol/special character
        
        combo = upper + lower + dig + spec  #combine all elements into one string
    
        password = password + random.choice(combo)  #select a random character from the combined sequence and add to password string
        count = count + 1 #increment count
        continue #continue with loop
    
    if count == length: #if count matches length (requested by user)
        return password #return the final password back

#testing function
print(genpwd(8))    
print(genpwd(10))    
print(genpwd(15))    
print(genpwd(-1))
#end of program
