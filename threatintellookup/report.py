import json
from log_parser.parse import count_map
from pathlib import Path
import csv

data = Path(__file__).parent / 'checked.json'

with open(data,'r') as f:
    checked = json.load(f)

#Category Count

category_list = []

for i,items in checked.items():
     category_list.append(items['usageType'])

category_count = count_map(category_list)

for i in category_count:
     print(f"{i} : {category_count[i]}") 

#Required Fields

dataset = {}

for i in checked:
    if checked[i]['usageType']:
        Category = checked[i]['usageType']
    Country = checked[i]['countryCode']
    Is_Whitelisted = checked[i]['isWhitelisted']
    Total_Reports = checked[i]['totalReports']
    dataset[i] = {'Category': Category, 'Country': Country, 'Is_Whitelisted': Is_Whitelisted, "Total_Reports": Total_Reports}

dataset2 = dict(sorted(dataset.items() , key = lambda x:x[1]['Total_Reports'],reverse=True))

# Top 10 most reported IPs

top_dict = []

for i,item in enumerate(dataset2.items()):
            if i<10:
                top_dict.append({"Rank":i+1,"IP_Address" : item[0], "Country" : item[1]['Country'], "Category" : item[1]['Category'],'Total_Reports' : item[1]['Total_Reports']})

print(top_dict)

with open('top_10.csv','w',newline='') as f:
     writer = csv.DictWriter(f, fieldnames= ['Rank','IP_Address','Country','Category','Total_Reports'])
     writer.writeheader()
     writer.writerows(top_dict)