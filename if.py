print ("The if statement")
a=10
b=50
if a>b:
    print ("a is greater than b")
elif b>a:
    print ("b is greater than a")
else:
    print ("Both are equal")

print ("---------------------------------")
print ("The Tuples")
names=('Vijay','Ajay','Showfic','Vj','Aj')
name=names[0::2]
print (name)

print ("----------------------------------")
print ("The Dictionary")
newdict={'Apple':100,'Orange':80,'Mango':60}
mydict=newdict['Apple']
print (mydict)

print ("---------------------------------")
print ("The list")
mylist=['Vijay',100,84.8]
print (mylist)
print ("Reassigning")
mylist=mylist[2]=98
print (mylist)
