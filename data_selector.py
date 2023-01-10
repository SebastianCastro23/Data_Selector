import csv

path = "example.csv"
data = []
avg = 5

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data = row
        
avg_list = []

for x in data:
    avg_list.append(abs(float(x)-avg))
    
min_list = sorted(zip(data, avg_list), key=lambda t: t[1])

print(min_list)
    
