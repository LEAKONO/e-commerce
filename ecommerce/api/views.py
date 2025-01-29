from django.shortcuts import render
from rest_framework import viewsets,generics,permissions
from .models import Product,Order
from .serializers import ProductSerializer,OrderSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from django.contrib.auth import login
from django.contrib.auth.models import User

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticated]

class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated]


class SignupView(generics.CreateAPIView):
    queryset=User.object.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.AllowAny]

class LoginView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=User.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        return Response({'error':'Invalid credentials'},status=400)