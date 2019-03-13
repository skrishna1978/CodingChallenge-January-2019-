#1.21.2019 - Shashi
#Take a number and print its sorted version in descending order
#Example: 1234 should become 4321
#Or 1734 should become 7431

def descendingSort(num):
  digitList = []
  for index in range(len(str(num))): #loop through the range of digits in original number
    digitList.append(str(num)[index]) #add them as strings into digitList

    digitList_sorted = sorted(digitList, reverse=True)  #create a sorted version of the string variable
    digitList_sorted_final = ''.join(digitList_sorted) #convert it back to integer with a "join"

  return int(digitList_sorted_final) #return final output back
  
#testing out the function with different values  
print(descendingSort(1734))
print(descendingSort(19784))
print(descendingSort(134))
