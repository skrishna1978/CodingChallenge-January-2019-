#1.24.2019 - Shashi
#program that accepts 2 lists and removes all values from list 1 that match list 2.
#so, if the lists are: 1,2,3,3,3,4,5  and list 2 is 3,4
#it should remove 3,4 from list 1 and return 1,2,5

def removeItems(list1, list2): #function starts here
    for value in list2: #loop through each value in list 2
        while(value in list1): #for each while as long as that value exists in list 1
            list1.remove(value) #remove it from list 1
        #loops end    
        
    return list1 #return updated list1

#test function
print(removeItems([1,2,2,2,3,3,4,5],[3,4])) #removes 3,4 from list
print(removeItems([3,3,4,6,6,6,7,8,9,10],[3,6,10])) #removes 3,6,10 from list
print(removeItems([101,87,23,23,244,109,-2],[-2,4])) #removes -2 but not 4 since it doesnt exist
#end of program
