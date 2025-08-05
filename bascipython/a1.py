num = "abc"

print(type(num))

x="hello world"
print(type(x))

x="20"
print(type(x))

x="20.5"
print(type(x))

x="1j"
print(type(x))

x=["apple","banana","cherry"]
print(type(x))

x=("apple","banana","cherry")
print(type(x))

x=range(6)
print(type(x))

x={"name":"John","age":36}
print(type(x))

x={"apple","banana","cherry"}
print(type(x))

x=frozenset({"apple","banana","cherry"})
print(type(x))

x = True
print(type(x))

x=None
print(type(x))


#int
 
x=10
print("checking datatype of x",type(x))
str1=str(x) #converting interger to string
print("checking datatype of str1",type(str1))
float1=float(x) #converting interger to float 
print("checking datatype of float",type(float1))
print(float1)


#float
 
x=20.5
print("checking datatype of x",type(x))#this is float
str1=str(x)
print("checking datatype of str1",type(str1)) #this is string
print(str1)
 
int1=int(x)
print("checking datatype of int1",type(int1)) #this is imterger 
print(int1)


#str

num="10"
print("checking datatype of int1",type(int1))
print(int1)

flt=float(num)
print("checking datatype of int1",type(flt))
print(flt)


number=20
#method1 using only if
if number==10:
    print("the number is 10")


number=20
#method2 using only if and else
if number==10:
    print("the number is 10")
else:
    print("the number is not 10")


number=20 
#method3 using if and elif
if number==10:
    print("thr=e number is 10")
elif number==20:
    print("the number is 20")
elif number==30:
    print("the number is 30") 


number=20
#method4 using if amd elif and else
if number==10:
    print("the mnumber is 10")
elif number==20: 
    print("the number is 20")
elif number==30:
    print("the number is 30") 
else:
    print("the number is not 10,20,30") 


#chained condition
x=5

if x<10:
    print("number is less than 10",x)


if x>15:
    print("number is less than 15",x)


#ternary oprerator

n=5

print("odd" if n % 2 !=0 else "even")


#nested conditions

x=5
if x>0:
    if x<10:
        print("x is positive single-digit number")
    else:
        print("x is a positive number,but not a single-digits")
else:
    print("x is not a positive number")


#if condition
x=5
if x>0:
    print("x is positive single-digit number" )

#if else
x=5
if x>0 and x<10:
    print("the numbr is positive and single-digit ")
elif x>0 and x>=10:
    print("the number uis positive and not single digit")
else:
    print("the number is not positive")


