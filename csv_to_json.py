import csv
import json

csvfile = open('data.csv', 'r')
jsonfile = open('data.json', 'w')

fieldnames = ("person_id","datetime","floor_level","building")
fieldfixers = {
    'floor_level': int
}

fieldfixers2 = {
    'datetime': str
}
reader = csv.DictReader(csvfile, fieldnames)
header = reader.fieldnames
a_line_after_header = next(reader)

for row in reader:
    for key,value in row.items():
        ffunc = fieldfixers.get(key)
        if ffunc:
            row[key] = ffunc(value)

        ffunc = fieldfixers2.get(key)
        if ffunc:
            row[key] = ffunc(value.replace(" ","-"))
    json.dump(row, jsonfile, sort_keys=False, indent=4, separators=(',', ':'))
    jsonfile.write(',')
    jsonfile.write('\n')

jsonfile.close()