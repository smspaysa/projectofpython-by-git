#i=0
#while i<10:
 #   print(i)
  #  i+=1

# i=0
# sum=0
# while i<=10:
#     sum+=1
#     i+=1
# print("sum",sum)    

# i=10
# sum=0
# while i<=20:
#     if i%2 ==0:
#         sum+=1
#     i+=1
# print("sum",sum) 

# i=10
# sum=0
# while i<=20:
#     if i%2!=0:
#         sum+=1
#     i+=1
# print("sum",sum) 

# x=0
# while True:
#     if x==4:
#         print("break from loop")
#         break
#     print("value are",x)
#     x+=1

# x=0
# while x<=10:
#     if x==4:
#         print("skip print 4 from loop")
#         continue
#     print("value are",x)
#     x+=1
 
#1
#12
#123
#1234
#12345

# for r in range(6): #r=3
# for c in range(r):#c=0,1,2
#         print(c+1,end="")
#     print()


#string method
# s="Hello,World!"
# print(s.replace("World","Python")) #output:"Hello ,Python!"
# print(s)

# s="Hello World"
# s=s.replace("World","Python")
# print(s)

# #lower
# s="Hello,World!"
# print(s.lower()) #output:"hello ,world!"

# #upper
# s="Hello,World!"
# print(s.upper()) #output:"HELLO,WORLD!"

# #title
# s="Hello,World!"
# print(s.title()) #output:"Hello ,World!"

# #
# s="    Hello,World!    "
# print(s.lstrip()) #output:"Hello ,World!    "

# s="    Hello,World!    "
# print(s.rstrip()) #output:"   Hello ,World!"

# s="    Hello,World!  "
# print(s.strip()) #output:"Hello ,World!"

# s="##########HelloWorld###############"
# print(s.lstrip("#"))

# s="##########HelloWorld###############"
# print(s.rstrip("#"))

# s="##########HelloWorld###############"
# print(s.strip("#"))

# print(s.split("#"))

# #split
# s="Hello,World!"
# print(s.split()) #output:["Hello,","World!"]

# s= ['Hello' , 'World!']
# print("$".join(s))

# s="12345"
# print(s.isdigit()) #output;true

# num1=int(input("enter the number1: "))
# num2=int(input("enter the number2: "))


# result=num1+num2
# print("sum of{}+{} is ".format(num1,num2),result)

# print(f"sum of{num1}+{num2} is",result)

# value="#############hello world################"
# s=value.strip("#").title().split()
# print("".join(s))

#creating a list of integers
# numbers=[1,2,3,4,5]
# print(numbers[2])

# #creating a list of string
# fruits=['appple','banana','cherrry']
# print(fruits[0])

# #creating a mixed-type list
# mixed_list=[10,'hello',True,3.14] 
# print(mixed_list[3])

#for loop
# fruits=["apple","banana","cherry","pine","orange"]
# for x in fruits:
#     print(x)
#OR
# for i in range(len(fruits)):
#     print(fruits[i])

#how many letter are there in it show
# name="aabcccd"
# print(name.count("a"))


# fruits=["apple","banana","cherry","pine","orange"]
#.count number of"a"

# for x in fruits:
#     counter=x.count("a")
#     if counter==1:
#       print(x)

# for i in range(len(fruits)):
  
#     counter=fruits[i].count("a")
#     if counter==1:
#        print(fruits[i])    

# #updates
# fruits=["apple","banana","cherry","pine","orange"]
# fruits[2]="aaa"

# #insert at end 
# fruits.append("pineapple")
# print(fruits)

# #insert at any position
# fruits.insert(2,"hello")
# print(fruits)

# #remove
# fruits=["apple","banana","cherry","pine","orange","apple"]
# fruits.remove("apple")
# fruits.remove("apple")
# print(fruits)

# #empty list ko lai append used it
# fruits=[]
# fruits.append("apple")

# #sort
# #ascending sort
# number=[1,7,3,8,4]
# number.sort()

# #descending sirt
# number=[1,7,3,8,4]
# number.sort(reverse=True)

#A_Z and a_z sort
# fruits=["a","b","z","y","z","c"]
# fruits.sort()

# name=["rama","ramesh","abc"]
# name.sort()




# matrix=[
#     [0,1.2],
#     [3,4,5],
#     [2,8,9]
# ]
# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])

# lst=[1,2,3,4,5]
# print(sum(lst))


# 
# matrix=[
#     [0,1.2],
#     [3,4,5],
#     [2,8,9]
# ]
# result=0
# for x in matrix:
#     result=result+sum
# print("result",result)
# print(sum(x))


# number=[1,3,6,4,2]
# number.sort()
# # number.sort(reverse=True)
# print(number)

#A_Z 
fruits=["zoo","cat","ball","apple","banana"]
fruits.sort()
# fruits.sort(reverse=True)
print(fruits)


#copy(the same address) shallow copy
lst1=[1,2,3]
lst2=lst1

print("lst1",lst1)
print("lst2",lst2)

lst1.append(4)
print("after append lst1",lst1)
print("after lst2",lst2)

#deep copy
# lst1=[1,2,3]
# lst2=lst1.copy()

# print("lst1",lst1)
# print("lst2",lst2)

# lst1.append(4)
# print("after append lst1",lst1)
# print("after lst2",lst2)


#list comprehensive(it is not list comp)
# fruits=["apple","banana","cherry","pine","orange"]
# output=[]

# for x in fruits:
#     print(x)
#     if "a" in x:
#         output.append(x)

#         print(output)

# list comprehensive ,when there is only if condition
fruits=["apple","banana","cherry","pine","orange"]
output=[x for x in fruits if "a" in x]        

#list comprehensive using if else
number=[1,2,3,4,5]
#output=["even","odd"]
output=["even"if x%2==0 else "odd"  for x in number]


#when there is no condition
fruits=["apple","banana","cherry","pine","orange"]
#output =capital
output=[x.upper() for x in fruits]

#apply list
lst=[]
print(type(lst))
#single value in list
lst=[1]
print(type(lst))

#empty tuple (single element in tuple)
number=(1,)
print(type(number))


#add remove update tuple
number=(1,2,3
        )
lst=list(number)
print(lst)
lst.append(4)
print(lst)

number=tuple(lst)


#unpacaking
tup=(1,2,3)
x,y,z=tup
print(x)
print(y)
print(z)

tup=(1,2,3,4,5)
x,y,*z=tup
print(x)
print(y)
print(z)

tup=(1,2,3,4,5)
x,*y,z=tup
print(x)
print(y)
print(z)

tup=(1,4,2,3)
*x,y,z=tup
print(x)
print(y)
print(z)


##
number=[1,2,3,4,5]
output=["even"if x%2==0 else "odd"  for x in number]

