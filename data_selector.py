import csv, itertools

def closest_value(list, value):
    difference = lambda list: abs(list-value)
    closest = min(list, key=difference)
    return closest

path = "EDX_Data.csv"
data = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data = row                                                  # lee y guarda todos los valores de la columna en una lista
        avg = float(data.pop(len(data)-1))  
    
        data = [float(i) for i in data]                                                                                        
    
        combinations = list(itertools.combinations(data,5)) 
        avg_list = []
        for x in combinations:
            avg_list.append(sum(x)/5)
    
        print(closest_value(avg_list, avg))
        print(combinations[avg_list.index(closest_value(avg_list, avg))])