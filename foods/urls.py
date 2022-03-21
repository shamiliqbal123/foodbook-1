

from django.urls import path
from.views import *

urlpatterns = [
   
  path('Categorylist',categoryadding.as_view()),
  path('Categorylist/<int:pk>',ItemApiView.as_view()),
  path('CategoryAdding',CreateCategory.as_view()),#Admin
  path('ItemAdding',CreateItem.as_view()),#Admin
  path('OrderList',OrderView.as_view()),
  path('OrderList/<int:pk>',OrderItemView.as_view()),
  path('OrderCreateList',ordercreate.as_view()),
  path('to/<int:pk>',TodaySpecial.as_view()),#Admin
  path('too',TodaySpecialItems.as_view()),#Admin
  path('register/', RegisterAPI.as_view(), name='register'),
  path('login/', LoginAPI.as_view(), name='login'), # Admin
  path('Popular/<int:pk>', Popular.as_view()),
  path('PopularItem', PopularItems.as_view()),
  path('Offer/<int:pk>',Offer.as_view()),
  path('OfferItem',OfferItems.as_view()),


]
