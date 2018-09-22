

data = "Hello Mr. Shailesh Sahu where are you from what you do normally!"
print(data) #Normal String

#There is no character variable in 
#python so that means string length of 1 is character

#some default string function
print(data[1])
print(data[2:6])
print(data.split(" "))
print(data.lower())
print(data.upper())
print(len(data))
print(data.strip())
print(data.replace("H","N"))



# read from user 
print("Please enter your name")
x = input()
print("Hello! "+x)