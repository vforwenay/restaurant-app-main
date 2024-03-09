from datetime import datetime
from restaurant.models import Item, Restaurant, Menu
from rest_framework import viewsets
from .serializers import CurrentDayMenuSerializer, ItemSerializer, RestaurantSerializer, MenuSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CurrentDayMenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Menu.objects.filter(created_at__date=datetime.now().date())
    serializer_class = CurrentDayMenuSerializer
