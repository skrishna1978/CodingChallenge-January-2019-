#1.4.2019
#Program to count how many ways a number can be added from 1 to N.
#Example : sum_ways(3) > 1+1+1, 2+1, 3+0 > 3 ways
#sum_ways(5) > 1+1+1+1+1, 1+4, 2+3, 0+5, 1+1+3, 1+1+1+2, 1+2+2 > 7 ways

def sum_ways(n): #function accepts the initial number
   return recur_sum(n, 0, 1) #recursive call to function that does the counting
   
def recur_sum(n, current, index): #params: initial number, 0 and 1.
    if current == n: #if n already current value, return 1
        return 1
    if current > n: #if current value greater than initial number, return 0
        return 0
    
    count = 0 #else we start counting 
    for i in range(index, n+1): #first pass: loop from 1 until (n+1)
        count += recur_sum(n, current+i, i) #recursive call that incrementally adds to counts value as long as loop is true
        
    return count #return count when loop done.
    
#test function with diff. values
num =10
print("There are",sum_ways(num), "ways to add", num)
num=15
print("There are",sum_ways(num), "ways to add", num)
num=5
print("There are",sum_ways(num), "ways to add", num)
