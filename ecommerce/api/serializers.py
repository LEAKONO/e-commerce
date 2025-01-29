from rest_framework import serializers
from .models import Product, Order
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs={'password':{'write_only':True}}
    def create(self,validate_data):
        user=User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password']
        )
        return user
class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model=Product
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields='__all__'