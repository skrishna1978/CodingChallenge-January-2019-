#1.8.2019 - Shashi
#program to autogenerate hashtags based on string inputs
#conditions : no spaces, first letter of each word uppercase, length <=140 and non-empty.

def gen_hash(s):
    if not s:
        return False #check for empty string
    else:
        s= s.title()    #capitalize first letter of every word
        s = s.replace(" ","") #get rid of all size spaces
        
        if len(s) < 140: #if length of final output is <140 characters
            return '#'+s #return hashtag
        else:
            return False #else return false
    
print (gen_hash("coding   total rox")) #regular string with diff. size spacing
print (gen_hash(" o n e ")) #single character check
print (gen_hash("cs education chat a")) #combination check
print (gen_hash("")) #empty string check
print (gen_hash("sO2a7fTQx7Ls0Ca5RJj1CnTWxVyQtQWm0BVfAFtPtLqL8HflVsTIYos3OILHAzXqEDDNrTBVXawrs7xmh1cDdRRKda6JlNmU0yPvXOLE2z6QruByD0F3bUiCueK3WZ5zUhpZGN4XCzg2")) #long text
#end of program
