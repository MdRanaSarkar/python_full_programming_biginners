"""

if expression:
    statement(s)
else:
    statement(s)

"""
"""
amount=int(input("Enter amount :"))
if amount<1000:
    discount=amount*.05
    print("if discount: ",discount)
else:
    discount = amount * .1
    print("else discount :",discount)
print("Net payable : ", amount-discount)

"""

"""
while expression:
    statement
"""
#print 0 to 9 using while loops
"""
count=0
while(count<10):
    print("The count :",count)
    count=count+1
print("Good Bye")


count=0
for i in range(10):
    print("The count :", count)
    count = count + 1

print("Good Bye in from for loop")
"""

"""
print it 
1 2 3 4 5 6 7 8 9 10 
4 6 8 10 12 14 16 18 202 
3 6
4 8
5 10 
6 12
7 14
8 16
9 18 
10 20

for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k,end=' ')
    print()

"""
k=['mango','apple','banana']
for i in k:
    print(i)