import math

def jump_search(seq, search):
     #empty list 
    if len(seq) == 0:
        return "empty list"
    
    else:
        #i know it said to assume acending order but you can never be too careful 
        seq = sorted(seq)
        jump = int(math.sqrt(len(seq)))
        i = 0
       
        
        for i in range(0, len(seq), jump):
            if seq[i] > search:
                break
            #if the jump is where the value is then it finds it here
            if seq[i] == search:
                return str(search) + " is at index " + str(i)
        else:
            # if loop exited normaly - add interval to i, so last chuck is included too
            i += jump
        #find chonk that you actually need to look at instead of the whole list
        chonker = seq[i - jump:i]
        #return chonker
        #easy way to look for something in a list
        
        if search in chonker:
            return str(search) + " is at index " + str(chonker.index(search)+ i-jump)
        else:
            return str(search) + " is not in list"

print(jump_search([1,2,3,4,5,6,7,8,9,10],5))
