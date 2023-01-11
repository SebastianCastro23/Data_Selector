import csv

path = "EDX_Data.csv"
data = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data = row                                                  # lee y guarda todos los valores de la columna en una lista
        avg = float(data.pop(len(data)-1))                                # elimina y establece el último valor como el promedio con el que 
                                                                    # compararemos los datos  
        distances = []                                              # aquí guardaremos las distancias entre cada dato y el promedio

        for x in data:
            distances.append(abs(float(x)-avg))                     # calculamos y guardamos cada distancia en la lista
    
        min_list = sorted(zip(data, distances), key=lambda t: t[1])  # aquí organizamos la lista de datos por la lista de distancias

        for i in range(0,5):
            print(min_list[i][0])
            
        print("___________")