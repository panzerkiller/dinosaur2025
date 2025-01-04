seats = 5000 # initial number of seats
while seats > 0: # seat available?
    if (seats-3) % 17 == 0: 
        print (seats)
    seats = seats - 1 # number of seats updated
    #print (seats)