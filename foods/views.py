from django.contrib.auth import login
from unicodedata import category
from django.shortcuts import render
from.models import MenuItem,Category,OrderItems,OrderStatus
from .serializer import CategorySerializer, ItemSerialilzer, OrderSerialilzer, OrderItemSerializer, ordercreate, \
    TodaySerializer, RegisterSerializer, PopularSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
# Create your views here.


class categoryadding(ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()

class ItemApiView(ListAPIView):
    serializer_class= ItemSerialilzer
    
    def get_queryset(self):
        return MenuItem.objects.filter(category=self.kwargs['pk'])

class OrderView(ListAPIView):
    serializer_class=OrderSerialilzer
    queryset=OrderStatus.objects.all()
class OrderItemView(ListAPIView):
    serializer_class=OrderItemSerializer
    def get_queryset(self):
        return OrderItems.objects.filter(order=self.kwargs['pk'])


class ordercreate(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class=ordercreate
    queryset=OrderStatus.objects.all()

    
#admin
class CreateCategory(CreateAPIView):
    serializer_class= CategorySerializer
    queryset=Category.objects.all()
class CreateItem(CreateAPIView):
    serializer_class= ItemSerialilzer
    queryset=MenuItem.objects.all()
class TodaySpecial(APIView):
    serializer_class=TodaySerializer
    
    def get(self, *args, **kwargs):
        booking = MenuItem.objects.get(id=kwargs['pk'])
        booking.today_special = True
        booking.save()
        return Response("Added")   

class TodaySpecialItems(ListAPIView):
    serializer_class=ItemSerialilzer
    queryset=MenuItem.objects.filter(today_special=True)


class Popular(APIView):
    serializer_class = PopularSerializer

    def get(self, *args, **kwargs):
        popular = MenuItem.objects.get(id=kwargs['pk'])
        popular.popular_item = True
        popular.save()
        return Response("Added")


class PopularItems(ListAPIView):
    serializer_class = ItemSerialilzer
    queryset=MenuItem.objects.filter(popular_item=True)



# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
        
        
        
