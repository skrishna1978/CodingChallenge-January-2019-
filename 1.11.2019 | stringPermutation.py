#1.11.2019 - Shashi
#Program to print permutations of diff. words in a string array

from itertools import permutations  #to user permutations() function for a list 

def sloganGen(array):
    list1=array #the array that came in
    list2=[] #new blank array to hold unique values and generate permutation combos

    for eachword in list1: #every word in original list
        if eachword not in list2: #if word doesn't exist in blank array
            list2+=[eachword] #add it
    
    list3=list(permutations(list2)) #generate all permutations of list2 and return to list3
    list3=[" ".join(x) for x in list3] #add new versions of list3 with each looping
    
    return list3 #return final list back to calling function
    
combos = sloganGen(["world", "coding"]) #send words via an array
print(*combos, sep='\n') #print it so that each array element is on a new line for better readability
print("\n") # new line for spacing
combos = sloganGen(["daily", "coding", "challenge"])
print(*combos, sep='\n')
#end of program
