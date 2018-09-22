
a=10
b=20

if a > b:
	print("1"+a)
elif a > 10:
	print("2"+a)
else:
	print("3")
	print(a)

if b > a : print("b is greater than a")

print("A") if a < b else print("B")

if b > a and a == 10 or a == 20:
	print("equal")