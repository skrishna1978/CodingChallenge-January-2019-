#1.19.2019 - Shashi
#write a function that takes starting and stopping numbers
#print out all the prime numbers who remain prime on reversing them too. Like 31. or

def backwardsPrimeRange(startNum, stopNum): #function starts here
    primeList = [] #make an empty list to load up every prime number found
    for value in range(startNum, stopNum): #loop from starting to ending value
        if isPrimeNum(value): #if number in range is a prime number
            primeList.append(value) #add it to the primeList array
    #end of for loop
    
    reversePrimeList =[] #make an empty list to hold those values that are prime even when reversed
    for value in primeList: #check each value in prime numbers list
        if isPrimeNum(int(str(value)[::-1])): #if reverse version of the number is also prime
            if value!=int(str(value)[::-1]): #and if reversed value is NOT EQUAL to its original number (example: 11)
                reversePrimeList.append(value) #add it to reverse prime number list
    #end of second loop
    
    return reversePrimeList   #return final list to calling function

#function that is used to check if a number is prime
#divisible only by itself and 1.
def isPrimeNum(num):
    for value in range(2,num-1): #loop from 2 ... until num -1
        if num%value==0:    #if any of those values divide the number
            return False    #not prime. so return false.
    #end of loop        
    return True #if loop reaches here then it is prime. return true.
    

print(backwardsPrimeRange(3,300)) #print all prime numbers between 3 and 300 that are prime on reversed too.
print(backwardsPrimeRange(1000,1100)) #testing for other large values
print(backwardsPrimeRange(90,190)) #testing for smaller values.
