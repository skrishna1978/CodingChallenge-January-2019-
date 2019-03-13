#1.13.2019 - Shashi
#Domain name extractor

def extractDomain(url): #function starts here
    
    if(not url):    #if invalid or empty string sent
        return False    #return False (or an error message)
    else:
        URLparts = url.split('.')   #split string based on period symbol (.) and store in URLparts[]
    
        if 'www' in url: #if the original string has 'www' in it
            return URLparts[1]  #return the 2nd item in URLParts[]
        elif '://' in url: #if string has "://" in the url
            return URLparts[0].split('://')[1]  #split array[1] element by :// and return 2nd element from resulting data 
        else:
            return URLparts[0] #if no www or :// then return the very first element in the URL
        
#test function with diff. types of inputs.
print(extractDomain("https://example.com/addition/actor.php"))
print(extractDomain("https://brother.example.org/?bells=back&authority=afterthough"))
print(extractDomain("https://www.example.com/"))
print(extractDomain("stackoverflow.com/questions/112121/coderhelp"))
print(extractDomain(""))
#program ends here
