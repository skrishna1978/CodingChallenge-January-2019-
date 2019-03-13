#1.28.2019 - Shashi
#Write a function that accepts a list and N. Return a list that contains elements of original list at most N number of times. Delete the rest.
#The order of the list elements should be unchanged.
#Example: [1,2,3,1,2,1,2,3] and N = 2.
#Output is [1, 2, 3, 1, 2, 3] because 1,2,3 should appear in list at MOST 2 times only.

def nOccurences(list,nMax):
	appearances = {} #dictionary that holds values and associated # of times it appears. Example: {25: 3}
	finalList = [] #array to  hold final array data
    
	for number in list: #for every number in the original list
    	if number not in appearances:   #does that number appear in occurrences?
        	appearances[number] = 0  #if it doesn't then make appearances[that number] = 0 (as in no appearances)
       	 
    	if appearances[number] < nMax:   #now check if appearance count for that number is < max allowed
        	appearances[number] = appearances[number] + 1  #if it is then add 1 to that count
        	finalList.append(number) #add that number to finalList
       	 
    
	#loop continues for other numbers in original list   	 
	return finalList #return the updated final list back
    
    
#end of function

print(nOccurences([1,2,3,1,2,1,2,3],2))  #print numbers for up to 2 occurrences only. ignore the rest.
print(nOccurences([101,201,113,123,201,101,222,34],1))  #print numbers for up to 1 occurrence only. ignore the rest.
#end of program
