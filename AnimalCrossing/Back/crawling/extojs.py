import xlrd
from collections import OrderedDict
import json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('D:\MJ\git\s02p31a403_ac\AnimalCrossing\Back\crawling\data\\fish.xlsx')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
data_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    data['pattern'] = row_values[0]
    data['response'] = row_values[1]
    data_list.append(data)
data_list = {'intents': data_list} # Added line
# Serialize the list of dicts to JSON
j = json.dumps(data_list)
# Write to file
with open('data1.json', 'w') as f:
    f.write(j)