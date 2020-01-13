def insertionSort(this):
    # want to swap with the one before if we have to 
    for x in range(1, len(this)):
        #second value gets saved
        temp = this[x]
        #i is index
        i = x
        #while index is larger than 0 AND the value of one less
        while i > 0 and this[i - 1] > temp:
            #swapping it down here
            this[i] = this[i - 1]
            #moves down the list, the whole way until nothing is bigger
            i -= 1
            
        this[i] = temp
    return this
