list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

#list1.pop(0) # remove data using index syntax
#print(list1)
# add math to 1 number index
"""
list1.insert(1,'math')
print("after inserting ",list1)
print(len(list2))
"""
"""
tup=tuple(list1)

print(tup)
print("showing 0 index value : ",tup[0])
print("len of tuple data : ",len(tup))
tup1=tuple(list2)

print("min value of  tuple data : ",max(tup1))


"""

"""
details about dictionary 

"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1={'village':"Dangapara","Thana":'Gulsan'}
dict.update(dict1)

print ("dict['Name']: ", dict['Name'])
dict['Age']=19
print(dict)

"""for printing only key 
for key in dict:
    print(key)
    """
"""for printing only values 

for value in dict.values():
    print(value)
"""
for key,value in dict.items():
    print(key, ':', value)