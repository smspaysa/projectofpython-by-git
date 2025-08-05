import csv
#Reading csv file usimg csv.reader
file_path="C:/basicpython/bascipython/data.csv"
with open(file_path,mode='r')as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)#Read the header row
    for row in csv_reader:
        print(row)


        # https://www.w3schools.com/python/pandas