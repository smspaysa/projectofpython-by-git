for x in range(10):
    print("Hello World")


#sum of 0-100
sum=0
for x in range(100):
    print("x",x)

    sum=x+sum
print("sum",sum)


#50-100 range(begin,end) it should always in interger so it kept in range
for x in range(50,100):
    print(x)

    sum=sum+x
    print("sum",sum)

#range(begin,end,step)step is for jump
for x in range(0,10,4):#in 4 3 skip
    print(x)


#print even number between 50-70
for x in range(50,70,2):
    print (x)

#print odd number between 60-80
for x in range(61,80,2):
    print(x)

#
string1= "abcdef"

lst1=[1,2,3,4,5,6]

tup1=(1,2,3,4,5)

for x in string1:
        print(x)


#
string123="aa bbb cccc ddddd eeee ffffff"
count_a=0
count_b=0
count_c=0
count_d=0
count_e=0
count_f=0

for x in string123:
    if x=="a":
         count_a+=1#count_a=count_a+1
    elif x=="b":
         count_b +=1
    elif x=="c":
         count_c +=1
    elif x=="d":
         count_d +=1
    elif x=="e":
         count_e +=1
    elif x=="f":
         count_f +=1
         





               