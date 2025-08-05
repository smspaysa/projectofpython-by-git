#normal code

# def add(x,y):
#     result =x+y
#     return result
# result=add(5,10)

#lambda code
# add =lambda x,y:x+y
# result=add(5,10)

square=lambda x:x**2
print(square(5))
#map
number=[1,2,3,4,5]
squared=list(map(lambda x:x**2,number))
#filter
number=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,number))