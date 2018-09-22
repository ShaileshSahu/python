#set are unordered and changeable but they don't are indexed means they might changed
# they are declared by curly braces

color = {"skyblue","purple","pink","violet","blue","teal","yellow","lightyellow","firebrick"}
data = set(("red","blue"))
print(color)

#Once the set is declared you can't change it's item but add it
#for adding the new element
color.add("white")
print(color)

#multiple element can be added by update method
color.update(["teal","magenta","silver","gold"])

for x in color:
	print(x)

print("black" in color)	


#to delete there is two method available discard and remove
color.remove("teal")
print(color)
color.discard("skyblue")
print(color)
color.discard("skyblue")
print(color)

#difference between remove and  remove raised error when not get element
#while discard doesn't raise

# color.clear()
print(color)
print(data)

# difference gives the result from the other list which left first
x = {"apple","mango","orange"}
y = {"blue","mango","orange"}
z = x.difference(y)
print(z)
# x.difference_update(y)
# print(x)


#intersaction gives the common element between two element
a=x.intersection(y)
print(a)
x.intersection_update(y)
print(x)

#disjoint return that two set are related or not

v = x.isdisjoint(color)
print(v)

e = x.issubset(y)
print(e)


#symetric difference and update
#means that element are having difference element came into
#the list

d = x.symmetric_difference(y)
print(d)
x.symmetric_difference_update(y)
print(x)


d = x.union(y)
print(d)









