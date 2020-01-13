 
def bubbleSort(this):
   
    x = len(this)
 
    #looking at all the values in the this. should be 0-9999 and 10000-1
    for n in range(x):
 
        # Last i elements are already in place
        for j in range(0, x-n-1):
 
            #looks at the value and the one next to it, if the first one is bigger then swap the order
            if this[j] > this[j+1] :
                this[j], this[j+1] = this[j+1], this[j]
 
    return this
