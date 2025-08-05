import csv
#writing data in csv file using Dictreader
file_path="C:/basicpython/bascipython/data.csv"
with open(file_path,mode='r')as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row['Name'],row['Age'],row['city'])