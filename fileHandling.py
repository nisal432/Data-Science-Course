# file = open("example.txt", "w")
# print(file.read())
# file.write("hello gg")
# print(file.read())

with open("example.txt", "w+") as file:
	file.write("hello guys how are you ")
	file.seek(0)
	print(file.read())
import os
print(os.listdir())
print(os.path.exists('example.txt'))
import pathlib
print(pathlib.Path("example.txt"))