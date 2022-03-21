from tkinter import Menu
# from typing_extensions import Required
from django.contrib.auth.models import User
from.models import MenuItem,Category,OrderStatus,OrderItems
from rest_framework import serializers
 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ItemSerialilzer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields="__all__"

class OrderSerialilzer(serializers.ModelSerializer):
    class Meta:
        model=OrderStatus
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=OrderItems
        fields=['id','item_quantity','item_total','item','order']
        read_only_fields=('order',)

class ordercreate(serializers.ModelSerializer):
    OrderItemss=OrderItemSerializer(many=True)
    class Meta:
        model=OrderStatus
        fields=['id','order_status','total','OrderItemss']

    def create(self,validated_data):
        OrderItemss=validated_data.pop('OrderItemss')
        order=OrderStatus.objects.create(**validated_data)
        for orderitem in OrderItemss:
            OrderItems.objects.create(**orderitem,order=order)
        return order

class TodaySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['today_special']

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['popular_item']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['offer_item']













# User Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user