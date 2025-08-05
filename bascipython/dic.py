student={
    "name":"Alice",
    "age":20,
    "grades":{
        'maths':90,
        'history':85,
        'science':95
    },
    'contact':{
        'email':'alice@example.com',
        'phone':'123-456-7890'
    }
} 
print("Name:", student['name'])
print("Maths grade:" ,student['grades']['maths'])
print("Email:", student['contact']['email'])
# print(student['name'])
# print(student['grades']['maths'])
# print(student['contact']['email'])
# print(student)