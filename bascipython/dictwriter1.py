import csv
data=[
    {'Name':'Alice','age':30,'city':'london'},
    {'Name':'Bob','age':25,'city':'Paris'},
    {'Name':'Charlie','age':15,'city':'Berlin'}
]
#writing Data to csv file using dictwriter
file_path='dictwriter.csv'
fieldnames=['Name','age','city']
with open(file_path,mode='w',newline='')as file:
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()#write header row
    for row in data:
        writer.writerow(row)