Data Parsing:

Write code to extract data from **data.csv**.
The data contains four columns. The first column is the person identifier. The second column is the datetime the person entered the floor. The third column is the floor the person accessed. The fourth column specifies the building the floor is in.
Each row is considered a floor access event. Your task it to output each floor access event in json format. Each event should comply with the schema located in **schema.json**.

Solution :

language used  : Python
Libraries : csv,json

Script : csv_to_json.py
csvFile : data.csv
josnFile : data.json

1. loading csv file and excluding headers  .
2. changing floor_level type from string to int
3. converting date_time in required format
4. dumping the data in data.json in json format .
