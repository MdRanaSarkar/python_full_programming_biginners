#required argument
def human(str):
    print("showing string :",str)
human("Rana")

#keyword argument

def humaninf(name,age):
    print('Name:',name)
    print('Age :',age)

humaninf("Rima",34)
print("for default arguments :")

def humaninf(name,age=20):
    print('Name:',name)
    print('Age :',age)
humaninf("shahnaj",30)
humaninf("Suborna")
# for return
def humaninff(a,b=20):
    return  a / b
a=humaninff(20,30)
print(a)

print("Anonymous function: ")
div=lambda a, b: a/b
print("after anonymous",div(20,30))

import math
print(dir(math))


