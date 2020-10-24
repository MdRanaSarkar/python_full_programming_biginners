import re
line="Cats are smaller than dogs"
matchobj=re.match(r'dogs',line,re.M|re.I)

if matchobj:
    print(matchobj.group())
else:
    print("No matching ")
    
searchobj=re.search(r'dogs',line,re.M|re.I)

if searchobj:
    print("After searching",searchobj.group())
else:
    print("No matching ")