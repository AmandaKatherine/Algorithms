def Fib_search(seq, search):
    #empty list
    if len(seq) == 0:
        return "empty list"
    else:
        #i know it said to assume acending order but you can never be too careful 
        seq = sorted(seq)
        #setting my two fib numbers
        #i got help on the fib number stuff from geeks for geeks
        fib2 = 0
        fib1 = 1
        fib = fib1 + fib2
        #have to find the fib numbers that will add up to the length of the list or greater so all the nums are included
        #like if you have a list of 12 things, you neeed fib 5 and fib 8 to make 13
        while (fib < len(seq)):
            fib2 = fib1
            fib1 = fib
            fib = fib1 + fib2
        index = -1;
       
        while (fib > 1):
            #here we check if seq[4] is the min value len-1 is indexing. if the seq[4] it too low, we down up the fib num
            i = min(index + fib2, (len(seq)-1))
            if (seq[i] < search):
                fib = fib1
                fib1 = fib2
                fib2 = fib - fib1
                index = i
                #If value is greater then we move down
            elif (seq[i] > search):
                fib = fib2
                fib1 = fib1 - fib2
                fib2 = fib - fib1
            else :
                return str(search) + " is at index " + str(i)
        if(fib1 and index < (len(seq)-1) and seq[index+1] == search):
            return index+1;
        return str(search) + " is not in the list"
print(Fib_search([1,2,3,4,5,6,7,8,9,10,11],12 ))
