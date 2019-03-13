#1.16.2019 - Shashi
#My first program in R programming language.
#Uses a function that accepts 2 numbers and outputs the running sum betwen the two.

sum_between <- function(n1, n2){
  total <- 0  #to hold the final value
  if (n1 == n2) #if both values are the same
  {  return (n1)  }  #return the same value back
  
  if (n1 < n2) #if first value lesser than second 
  { for (value in n1:n2) #loop from n1 to n2  
    { total = total+value }  #total up all the values
    return (total)  # return total after loop ends
  } #end if
  
  if (n2 < n1) #if second value lesser than first 
  { for (value in n2:n1) #move from lesser value to greater 
    { total = total+ value } #total up the values
    return (total) #return total after loop ends
  }#end if
}#end of functon sum_between()


sum_between(1,5)  #1+2+3+4+5 = 15
sum_between(10,5) #10+9+8+7+6+5 = 45
sum_between(6,6)  #6
sum_between(-5,5)  #0
