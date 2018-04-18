from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=250)
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	shipping_address = models.CharField(max_length=250)

class Cart(models.Model):
	card_code = models.AutoField(primary_key=True)
	total_price = models.IntegerField()
	paid = models.BooleanField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
	price = models.IntegerField()
	name = models.CharField(max_length=250)
	cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
