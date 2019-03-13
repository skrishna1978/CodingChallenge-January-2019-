#1.18.2019 - Shashi
#Take age of human and convert it to Cat and Dog years based on the following conditions:
#humanYears >= 1
#humanYears are whole numbers only
#Cat Years...
#15 cat years for first year
#+9 cat years for second year
#+4 cat years for each year after that
#Dog Years...
#15 dog years for first year
#+9 dog years for second year
#+5 dog years for each year after that

def humanCatDog(humanAge): #function begins
    catAge,dogAge=0,0 #base values for cat/dog years
    if humanAge == 1:           #if human age is 1
        catAge,dogAge=15,15     #both animal ages are 15
    elif humanAge>=2:           #if human age >=2
        catAge,dogAge=24,24     #both animal ages are 24
        for value in range(humanAge-2,0,-1):    #If human years after the 2nd year (such as 5) 
         catAge += 4                                     #keep adding 4 for every cat year and 5 for every dog year
         dogAge += 5        
         #end of loop
    return [humanAge,catAge,dogAge] #return all values back.


print("Years > [Human, Cat, Dog]",humanCatDog(5))
print("Years > [Human, Cat, Dog]",humanCatDog(3))
print("Years > [Human, Cat, Dog]",humanCatDog(7))
print("Years > [Human, Cat, Dog]",humanCatDog(-2))
print("Years > [Human, Cat, Dog]",humanCatDog(1))
