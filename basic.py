obj = {
	
	"subject" : "java",
	"name" : "nis",
	"number": 3
}
print(obj["subject"])
for key in obj:
	print(obj[key])
print(obj.keys())
print(obj.values())
print(obj.items())
print(type (obj.values()))
i = 0
while i<= 10:
	print(i)
	i = i+1
print(list(range(0,5,3)))
list1 = []
for i in range(1,22):
	list1.append(i*i)


print(list1)
def hello():
	print("hello")
hello()
def adapt(default = "nice"):
	"""Prints default if not given any argument"""
	print(default)
	return default
adapt(33)
print(help(adapt))
def unlimited(default = "game", *args, **kwargs):
	for value in args:
		print(value)
		print(kwargs)
unlimited('game', 1, 2, 3, 4, name = "solo")

def square(arg = 1):
	return arg**2
print(square(33))
