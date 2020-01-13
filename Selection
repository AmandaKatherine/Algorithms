def SelectionSort(this):
    #gotta go through the whole range
    for x in range(len(this)):
        # min is set to the first element while searching for the actual min 
        min = x
        #we can skip the 0th element because min is already set to that, through the whole range
        for i in range(x+1, len(this)): 
            #if min is bigger than any jth term, then a new min is set, because thats how mins work
            if this[min] > this[i]: 
                #have to save the new min
                min = i 
              
                #if we have a new min, we need to swap it so it moves down
        this[x], this[min] = this[min], this[x] 
    return this
