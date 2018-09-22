# Dictionaries is a collection which is unordered,changeable,and indexed
# and no duplicacy they are key value pair based

analysis ={
	"name":"TCS",
	"established":1981,
	"employee":12000040,
	"field":"IT"
}

print(analysis)

#first to get value
x = analysis["field"]
print(x)

#second to get value by get()
x = analysis.get("field")
print(x)


#change value 

analysis["year"] = 1982
print(analysis)


#loop thorugh the dictionary in the list worked
for x in analysis:
	print(analysis[x])


for x in analysis.values():
	print(x)


for x,y in analysis.items():
	print(x,y)


#adding item in the dictonary

analysis["description"] ="Service based industry"
print(analysis)

# removing the element through the system
del analysis["year"]
print(analysis)


