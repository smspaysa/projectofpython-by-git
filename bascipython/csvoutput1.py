import csv
data=[
    ['Alice',30,'London'],
    ['Bob',25,'Paris'],
    ['Charlie',15,'Berlin']
]

file_path="C:/basicpython/bascipython/output.csv"
with open(file_path,mode='w',newline='')as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(['Name','Age','city'])#writer header
    for row in data:
        csv_writer.writerow(row)