from django.db import models

class Customer(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=50, default="")
	address = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=20, default="")
	


class Order(models.Model):
	customerName = models.CharField(max_length=20, default="")
	address = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=20)
	order = models.CharField(max_length=100)

class Menu(models.Model):
	foodName = models.CharField(max_length=20)
	gramm = models.CharField(max_length=20)
	price = models.IntegerField()


class OrderDetails(models.Model):
	order = models.ForeignKey('Order', on_delete = models.CASCADE)
	menu = models.ForeignKey('Menu', on_delete = models.CASCADE)
	amount = models.IntegerField()
	
		
class Delivery(models.Model):
	orderNum = models.IntegerField()
	address = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=20)

class Payment(models.Model):
	amount = models.IntegerField()
	online = models.IntegerField()
	creditCard = models.IntegerField()


class Workers(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	email = models.CharField(max_length=20)
	startedDay = models.IntegerField()
	payment = models.IntegerField()
	phoneNumber = models.CharField(max_length=20)
	idPassword = models.IntegerField()
	gender = models.CharField(max_length=10)

class Staffs(models.Model):
	firm = models.CharField(max_length=30)
	firmAddress = models.CharField(max_length=30)
	phoneNumber = models.CharField(max_length=20)
	product = models.CharField(max_length=20)
	timetoBring = models.IntegerField()

class Products(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()
	quality = models.IntegerField()