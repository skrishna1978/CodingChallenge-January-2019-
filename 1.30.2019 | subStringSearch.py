#1.30.2019 - shashi
#search for a substring pattern within a given string

def substrCount(string, searchText):
  loop = 0  #controls the looping within the string
  counter = 0 #counter to hold how many matches were found
 
  if string and searchText:  #valid values
	while loop < len(string): #loop until string length maxes out
  	if string.startswith(searchText, loop): #check for portion of string with search text
    	counter = counter +1 #if true then increment counter
  	loop = loop+1 #loop progression
 	 
	return counter #once loop is done, return final value back
 
 
print(substrCount('abracadabra is absolute magic', 'br'))
print(substrCount('hocus pocus focus ', 'us'))
print(substrCount('hello world', 'xy'))
