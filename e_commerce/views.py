from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import datetime

from .models import User, Product, Cart
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .serialize import UserSerializer, ProductSerializer, CartSerializer

# Create your views here.
class Home(View):

    def get(*args, **kwargs):
        return HttpResponse('Hello, World!')

class UserView(APIView):
	def get(self, request):
		users = User.objects.all()
		serialize_account = UserSerializer(data=users, many=True)
		if serialize_account.is_valid():
			return JsonResponse(serialize_account.data)
		return HttpResponse(serialize_account.errors, status=400)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class ProductView(APIView):
	def get(self, request):
		products = Product.objects.all()
		serialize_account = ProductSerializer(data=products, many=True)
		if serialize_account.is_valid():
			return JsonResponse(serialize_account.data)
		return HttpResponse(serialize_account.errors, status=400)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = ProductSerializer(data=data) 
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class CartView(APIView):
	def get(self, request):
		carts = Cart.objects.all()
		serialize_account = CartSerializer(data=carts, many=True)
		if serialize_account.is_valid():
			return JsonResponse(serialize_account.data)
		return HttpResponse(serialize_account.errors, status=400)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = CartSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)