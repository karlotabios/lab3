from .models import User, Product, Cart
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'shipping_address')


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('price', 'name', 'description', 'cart')

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = ('cart_code', 'total_price', 'created_on', 'updated_on', 'paid')