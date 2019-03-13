#1.3.2019 - Shashi
#Write a program to find the sum of intervals of ranges in an array.
#overlapping intervals should only be counted once.

def sum_of_intervals(ranges): #function starts here
    sum = set() #to create a collection of items
    for x,y in ranges: #loop through all data sets
        for i in range(x,y): #loop within each data set
            sum.add(i) #add every number that is in that range.
    
    return(len(sum)) #every element added is contributing to sum. so size of final set returned.


print(sum_of_intervals([[1,2],[6,10],[11,15]])) #1+4+4 = 9
print(sum_of_intervals([[1,5],[3,6],[8,10]])) #1-5 and 3-6 have overlapping numbers. So, 1-6 = 5 and 8-10 = 2 = 5+2 =7
print(sum_of_intervals([[11,22],[6,10],[11,15]])) #11-22 covers 11-15 so 11. 6-10 = 4. So, 11+4 = 15.
#end of program
