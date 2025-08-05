# set1={"a","c","d","e","a"}
# print(set1)

# for x in set1:
#     print(x)

# set1={1,0,True,False,2,4}    
# print(set1)

# lst=[]
# tup=()

#empty set
# set1=set()
# set1={1}
# print(type(set1))

# set1={1,3,4,5,6}
# set1.add(2)
# print(set1)

# set1={1,2,3,4}
# set2={3,4,5,6}


#Dictionary
my_dict={
    "name":"Alice",
    "age":"30",
    "city":"New York"
}
# print(my_dict["Name"])
# print(my_dict.get("address"))
print(my_dict.get("address",123123123123))

my_dict["age"]=31
my_dict["gender"]="Female"

# print(my_dict)
# del my_dict["city"]
# print(my_dict)
my_dict.pop("age")
print(my_dict)

dict1={
    "name":"abc",
    "age":28,
    "phone":967734056
}
# for x in dict1.keys():
#     print(x)

for  k,v in dict1.items():# value same  time ma aauna use k,v and dict1.items instead of x and dict.keys(KEY AND value coe together)
    print(k,v) 


#Example of a nested dictionary representing
# student={
#     "name":"Alice",
#     "age":20,
#     "grades":{
#         'maths':90,
#         'history':85,
#         'science':95
#     },
#     'contact':{
#         'email':'alice@example.com',
#         'phone':'123-456-7890'
#     }
# } 
# print(student["name"])
# print(student['grades']['maths']) 

# modifying nested elements
# student['age']=21
# student['grades']['history']=88
# student['contact']['address']='123 main st'
# print(student)

#accessing nested  elements
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




