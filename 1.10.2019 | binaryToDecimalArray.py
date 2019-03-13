#1.10.2019 - Shashi
#program to accept binary value as an array and return its decimal equivalent.
#Binary code can be of any length but should only comprise of 1s and 0s.

def bin_dec(binArr): #function starts here
    result = 0 #variable to hold final answer
    for i in range(len(binArr)): #loop through each digit in the array
        if binArr[i] == 1:  #only 1 position elements have a power
            result = result + pow(2,len(binArr)-1-i) #total calculated by squaring arrpos(length-1-i)
            #We do this because digit powers start from right but array is being navigated from the left.
            #So for 1100, the first 1 is [0] in array but in position 3 as a number.
            #Hence, len(binArr)-1-i for that position gives u : len(binArr) = 4 -1-0 (since i is 0 at this point)
            #4-1-0 = 4 - 1 = 3. 2 power 3 is what we want for first 1.
            
            #continue loop for all elements in array
    return result #return output

print(bin_dec([1,0,0,1,1,1,1])) #79
print(bin_dec([1,1,1,1,0])) #30
print(bin_dec([1,0,0])) #4
print(bin_dec([1,0,1,0,0,1])) #41
#end of program
