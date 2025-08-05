# class Person:
#     def _init_(self,name,age):
#         self.name=name
#         self,age=age

#         def great(self):
#             return f"hello",my name is {self.name} and I am{self.age}years old".



#method of handling exception\
#method of try catch with any exception
# 
#method2 of try catch with exception
# try:
#     a=int(input("enter the number1:"))
#     b=int(input("enter the number2:"))
#     result=a/b
#     print(result)

# except Exception as e:
#     print(e)
#     a=int(input("enter the number1:"))
#     b=int(input("enter the number2:"))
#     result=a/b
#     print(result)    


#method3 custom exception with single exception handler
try:
    age=int(input("enter the age"))
    if age<0:
        raise Exception("you have entered negative in age")
    elif age==0:
        raise Exception("you have entered zero value in age ")
    print("my age is",age)


except Exception as e:
    print(e)
    print("invalid age")
    
