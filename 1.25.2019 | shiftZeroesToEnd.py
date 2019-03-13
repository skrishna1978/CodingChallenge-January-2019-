#1.25.2019 - shashi
#Program that accepts an array of different elements
#And moves all the integer 0s to the end of it. String 0s like "0" or "0.0" remain untouched.


def shiftZeroesToEnd(myArray): #function starts here
    zeroCounter = 0 #counter to keep track of how many 0s exist.
    shiftedArray = [] #array to hold final output
   
    for item in myArray: #loop through each item in array
        if (str(item) == "0" or str(item) == "0.0") and type(item) is not str:
            zeroCounter += 1 #if numeric string found, incremenet zero counter
        else:
            shiftedArray.append(item) #else add item from original list as is (same position)
    #end of loop        
    zeroStore = [0 for i in range(zeroCounter)] #declare an array of 0s of the size of zeroCounter
    shiftedArray.extend(zeroStore) #append it to final output list (adds it to the end)
    
    return shiftedArray #return final output back

#testing function
print(shiftZeroesToEnd([True, 3, 3, 0, 23, 0, 112, "b", "a"]))
print(shiftZeroesToEnd([0.0, 23, -3, False, "xxx", 0, 112, True , 9]))
