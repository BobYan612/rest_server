##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################

from django.urls import path, include
from .views import (product_list, product_detail, trolley_list, trolley_detail, UserViewSet, GroupViewSet, clear
,trolley_group_list, trolley_group_detail, credit_card_create, credit_card_detail, transact_payment)
from rest_framework import routers

"""
The url definition of the product and trolley
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('product/', product_list),
    path('product/<int:pk>/', product_detail),
    path('trolley/', trolley_list),
    path('trolley/<int:pk>/', trolley_detail),
    path('trolley_group/', trolley_group_list),
    path('trolley_group/<int:pk>/', trolley_group_detail),
    path('credit_card/', credit_card_create),
    path('credit_card/<int:pk>/', credit_card_detail),
    path('transaction/', transact_payment),
    path('clear/', clear)
]