"""
file mode :
r, rb ,r+ ,rb+ ,w ,wb,w+ ,wb+,a ,
"""

"""
Syntax
fileObject.write(string);


fo=open('new.txt','r')
fr=fo.readlines()
print("after reading the file : ",fr)
fo.close()

"""


"""
try:
 You do your operations here

except:
 If there is any exception, then execute this block.
 ......................
else:
 If there is no exception then execute this block.

"""
fo=open('new.txt','w')
try:
    fo.write("something")
except:
    print("You cannt write ")
else:
    print("successfully write")

