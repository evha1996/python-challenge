import os
import csv

from collections import Counter 
csv_reader = os.path.join("Resources","budget_data.csv")
with open(csv_reader, 'r') as f:
    
    reader = csv.reader(f)
   
    for row in reader:
        num_months = list(reader)
        row_count = len(num_months)
        print("Months:", row_count)
        
        



