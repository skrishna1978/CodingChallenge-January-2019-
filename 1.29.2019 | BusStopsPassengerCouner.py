#1.29.2019 - Shashi
#Program that processes people entering and exiting a bus at different bus stops.

def number(bus_stops): #function starts here
    onBusStill = 0 #to hold remaining count
    
    for stops in bus_stops: #process each item pair in list [col1,col2]
        onBusStill = onBusStill + stops[0] - stops[1]  #remaining count + people entering - people leaving
    #end of loop
    
    return onBusStill #return value back


print(number([[10,0],[3,5],[5,8]]))  
#Stop 1: 10 in, 0 out (10) | Stop 2: 3 in, 5 out (8) | Stop 3: 5 in, 8 out (5 remain)
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])) 
#3 in, 0 out (3) | 9 in, 1 out (11) | 4 in, 10 out (5) | 12 in, 2 out (15)
#6 in, 1 out (20) | 7 in, 10 out (17 remain)    
print(number([[3,0],[9,4],[4,8],[12,4],[6,5]]))
#3 in, 0 out (3)|9 in, 4 out (8)| 4 in, 8 out (4)| 12 in, 4 out (12)| 6 in, 5 out (13)
