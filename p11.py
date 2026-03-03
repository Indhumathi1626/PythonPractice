# Basic program for list
#compare two list anf find the common elements
a = [1,2,4,5,3,6,21,34]
b = [1,4,3,6,21]
c = []
for x in a:
    if x in b:
        c.append(x)       
print(c)        


   
