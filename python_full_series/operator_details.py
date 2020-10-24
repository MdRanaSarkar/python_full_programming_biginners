"""
arithmatic operator
+,-,*,/,%,,**,//


a=6%4
print("after modulas",a)

d=3**4 #3*3*3*3
print("after exponent",d)
e=10/3  #3.33333333
f=10//3  #3

print("after floor division",f)
"""

"""
*******comparison operator ***********
These operators compare the values on either side of them and decide the relation among
them.
operators:
==, !=,>,<,>=,<=

a,b =input().split()
c=int(a)
d=int(b)
if c>d:
    print("a=%d is greater than b= %d" %(c,d))
else:
    print("a=%d is not greater than b=%d" ,c ,d)



"""

"""
assignment operator 
=, +=,-=,*=,**=,/=,//=


a=4
print("a's value",a)
a**=6

print("a's value after exponent AND",a)
"""

"""
bitwise operator :
& Binary AND ,
| Binary OR
^ Binary XOR
~ Binary Ones Complement
<< Binary Left Shift
>> Binary Right Shift

a,b=60,13
c=bin(a)
d=bin(b)
print("after creating binary of a:",c)
print("after creating binary of b:",d)

e=a^b
print("after and operator binary of a:",bin(e))
f=~a
print("after ones complement of  a:",bin(f))




"""


"""
Python Logical Operators

and Logical AND,
or Logical OR,
not Logical NOT,

#Python Membership Operators
in,not in 

#Python Identity Operators
is ,is not


"""
a=5

b=a>6 and a<10
print("and operator checking ",b)
#or operator

b=a>6 or a<10
print("or operator checking ",b)
#not operator
b=not(a>6 and a<10)
print("not operator checking ",b)




#membership operator

x = ["apple", "banana"]
y = ["apple", "banana"]

z="apple"
print("membership operator",z in x)

#Python Identity Operators
i=x
print("identify op 1",x is i)
print("identify op 2",x is y)
print("identify op 3",x==y)

def oddchecking(n):
    if n&1==0:
        print("n is even number")
    else:
        print("n is odd number")
a=int(input("taking input"))
oddchecking(a)