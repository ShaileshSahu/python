# list is the one of the four collection data types in python
#property : ordered and duplicate members and changeable.

#Basic Defination of the list
_mylist = ["apple","mango","bannana","watermelon"] #square bracket way of defining the list
_color = list(("red","green","teal","skyblue","purple","tomato","green")) #by constructor concept 
_number = [4,5,2,45,62,0]
print(_mylist)

#index name to get particular name
print(_mylist[1])

#indexof used to get the index by name
print(_color.index("teal"))  #give the index 2

#change the current value by accessing the index
_mylist[1] = "graphes"

#count the number of the duplicates
print(_color.count("green"))
print(_mylist)

#for loop used to fetch the list
for x in _mylist:
	print(x)

#sort the list
_color.sort(reverse=False)     #ascending order would be reverse=False
print(_color)				   #Descending order would be reverse=True


#Reverse the order
_color.reverse()
print(_color)


#extend the list by the other list
_color.extend(_number)
print(_color)

#adding the new element in the list
print(len(_mylist))
_mylist.append("pineapple")
print(_mylist)

#insert the new element between the list
_mylist.insert(2,"orange")
print(_mylist)

# Delete the current and existing list
_mylist.remove("apple")
print(_mylist)

_mylist.pop()
print(_mylist)													

del _mylist[1]							#Difference between clear and del is that del delete the refrence of
print(_mylist)							#list after that variable become undefined while clear empty list							

_mylist.clear()
print(_mylist)

del _mylist
														

x =_color.copy()
print(x)
