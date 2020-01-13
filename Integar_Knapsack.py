def int_knap(csv9, capacity):
    
    
    import os
    import csv

    os.chdir(r'C:\Users\amand\Downloads')
    with open(csv9) as f:
        data=[tuple(line) for line in csv.reader(f)]
    name = []
    value = []
    weight = []
    for i in data:
        name.append(i[0])
        value.append(i[1])
        weight.append(i[2])
    
    #remove the labels 
    name.remove(name[0])       
    value.remove(value[0])
    weight.remove(weight[0])
    
    
    for i in range(0, len(value)):
        
        value[i] = int(value[i]) 
            
    for i in range(0, len(weight)): 
        weight[i] = int(weight[i]) 
              
    ratio = []
    
    ratio = [x/y for x, y in zip(map(int, value), map(int, weight))]
    #print(ratio)
    
        
    data = list(zip(name, value, weight,ratio))
    
    #this sorts by best for your buck sort of deal
    data  = sorted(data, key=lambda x: x[3], reverse=False)
    

    name = []
    value = []
    weight = []
    ratio = []
    for i in data:
           
        name.append(i[0])
        value.append(i[1])
        weight.append(i[2])
        ratio.append(i[3])
    
    #print(ratio)
    
   
    items = []
    i = len(weight)
    knapsack=[]
    total_weight = 0

   
    while capacity > 0 and i > 0:
        i-=1
        
        if weight[i] < capacity:
            capacity -= weight[i]
            total_weight+= weight[i]
            knapsack.append(name[i])
            items.append(value[i])
            del value[i]
            del weight[i]
            del name[i]
        
    #print(bag)
    return('We have packed ' + str(knapsack) , 'Our bag weights: ' + str(total_weight) , "The value of this bag is: " + str(sum(items)))

            

        #ratio.remove(ratio[i])                   
print(int_knap('Assignment9.csv', 550))   
