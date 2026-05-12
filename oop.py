class Animal:
	def __init__(self, type):
		name =input("Enter your dog name")
		self.type = type
		self.name = name
dog = Animal("Doggie")
print(dog.name)
class BankAccount:
	def __str__(self):
		return self.name
	def __init__(self,name, address, pin):
		self.name = name
		self.address = address 
		self.accountNumber = 0000000
		self.cardNumber = 111111
		self.balance = 0
		self.__pin = pin

	def deposit(self, amount):
		self.balance = self.balance + amount
		print("successfully deposited")
	
	def withdraw(self, amount):
		if self.balance < amount:
			print("YOu have less amount")
			return
		self.balance = self.balance- amount
		print('withdraw successful')
	
	def showBalance(self):
		pn = int(input("Enter your pin "))
		if pn == self.__pin:
			print("YOur balance is ", self.balance)
	
account1 = BankAccount("nischal", "bhaktapur", 14279)
print(account1)
account1.showBalance()
		