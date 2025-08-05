#typ1:parameter 
# def add():
#     a=10
#     b=20
#     result=a+b
#     print(result)
#     add()

#type:with parameter and non return type function
# def add(a,b):
#     result=a+b
#     print(result)

# x=5
# y=10
# add(x,y)

#typ3: with parameter and return type function
# def add(a,b):

#     result=a+b

#     return result
# final_result=add(5,6)#function call
# print(final_result)

#type4: parameter less and return type function
# def add():
#     a=6
#     b=10
#     result=a+b 
#     print(result)
#     return result
# final_result=add()
# print(final_result)


# def cal():
#     a=6
#     b=10
#     result1=a+b 
#     result2=a-b
    #lst=[]
    #lst.append(result2)
    #lst.append(result1)
    #return lst
#     return result1, result2
# final_result=cal()
# print(final_result)

# def add(a,b=0,c=1):#default argument
    
#     global x#access from outside
#     x=10
#     result=a+b 
    
#     return result
# final_result=add(5,6)
# print(final_result)
# print (x)


import matplotlib. pyplot as plt#()
x=[1,2,3,4,5]
y=[2,3,5,7,11]

x1=[6,7,8,9,10]
y1=[2,3,5,7,11]

plt.plot(x,y, marker='o',linestyle='--',color='b',label='Prime Numbers')
plt.plot(x1,y1,marker='o',linestyle='-',color='r',label='Numbers')

plt.xlabel('x Axis')
plt.xlabel('y Axis')
plt.title('Prime number Plot')

plt.legend()
plt.show() 