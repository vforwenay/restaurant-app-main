from django.contrib.auth.models import User
from rest_framework import serializers
from restaurant.models import Item, Menu, Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CurrentDayMenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    menu = MenuSerializer(read_only=True, many=True)
    class Meta:
        model = Item
        fields = '__all__'

