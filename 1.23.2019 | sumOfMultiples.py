#1.23.2019 - Shashi
#program that accepts 2 integers A, B and returns the sum of all multiples of A below B.
#B is excluded from the multiples
#ex: 2,9 = 2 + 4 + 6 + 8 = 20
#ex: 3,10 = 3 + 6 + 9  = 18

def sumOfMultiples(a, b):  #function starts here
    if a<=0 or b<=0:
        return('INVALID')   #take care of invalid values
    else:
        finalTotal=0    #else default is 0

        for number in range(a,b,a): #loop from A to B, incrementing by A values each time
            finalTotal+=number  #add on to the subtotal

        return(finalTotal)  #loop done, return final value back

#testing function
print(sumOfMultiples(2,10))
print(sumOfMultiples(2,9))
print(sumOfMultiples(-3,6))
#end of program
