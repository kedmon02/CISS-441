import csv
import json

row_count = 0
wine_data = []

# importing the csv file: each row is a list
with open('complete.csv', 'r') as csvfile:
    wine_stream = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    
    # This moves over the data file by row 
    for wine_row_dict in wine_stream:
        
        row_count += 1
        
        # only shows the first 5 rows.
        if row_count <= 10:
            print(row_count, wine_row_dict['region_1'], wine_row_dict['region_2'], wine_row_dict['variety'])
            
        wine_data.append(wine_row_dict)
        
print('I found this many rows in the csv', row_count)
with open('result.json', 'w') as fp:
    json.dump(wine_data, fp, sort_keys=True, indent=4, separators=(',', ': '))
