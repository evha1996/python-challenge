# import os
import csv
import statistics

total_months = 0 
total = 0 
month = []
rows = [] 
csv_path = "budget_data.csv"


with open(csv_path, 'r') as f:

    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += int(row[1])
        total_months += 1 
        month.append(row[0])
        rows.append(row)
       
differences= []

for idx, row in enumerate(rows):
    try:
        change = int(row[1]) - int(rows[idx + 1][1])
        differences.append(change)
    except IndexError:
        print('done')
        average_change = sum(differences)/len(differences)
        max_change = max(differences)
        min_change = min(differences)
        month_max_change = differences.index(max_change) # this is where I get stuck 



    
print("Net Profit:",total)
print ("Months:", total_months)
print ("Average Change:",average_change)
print(month_max_change) #trying to print associated month with max
print(min_change)

            








        
        



