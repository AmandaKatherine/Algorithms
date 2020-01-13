def binary_search(seq, search):
     #test case of 0
    if len(seq) == 0:
        return "empty list"
    else:
        #i know it said to assume acending order but you can never be too careful 
        seq = sorted(seq)
        #max and min indecies
        min = 0
        max = len(seq) - 1
        
        while True:
            if max < min:
                return str(search) + " is not in the list"
            m = (min + max) // 2
            #have to check if the index in seq value is less than search then we know we have to look at a bigger numbers
            if seq[m] < search:
                #reducing the amount of min to look at
                min = m + 1
                #if seqm is too big, then need to look at smaller values 
            elif seq[m] > search:
                max = m - 1
            else:
                return str(search) + " is located at index " + str(m) 
print(binary_search([2,3,2],1))
