#1.1.2019 - Shashi
#Write a program that accepts values via multiple function arguments
#and returns the sum of them back.

def add(num): #function call
    return SelfFunction(num) #call to SelfFunction() that holds retained and new value sums
    
class SelfFunction(int): #called as return function from within add()
    def __call__(self, num): #__call__ is a built in that returns a new instance of itself
        return SelfFunction(self + num) #returns last retained  + new number

#function calls for different sets of values
print(add(1)(4)(6))
print(add(13)(-5))
print(add(10)(6)(2)(9))
#end of program
