##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################
import traceback
import logging

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ProductPrice, ProductItem, Trolley, TrolleyList, Payment, CreditCard
from .serializers import (ProductPriceSerializer, ProductItemSerializer,
                          TrolleySerializer, GroupSerializer, UserSerializer, TrolleyListSerializer,
                          CreditCardSerializer, PaymentSerializer)
from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User

LOGGER = logging.getLogger(__name__)

@csrf_exempt
def clear(request):
    """
    Test purpose: to clean all objects created by other cases
    """
    if request.method == 'POST':
        users = User.objects.all()
        for user in users:
            if user.username != "admin":
                user.delete()
        payments = Payment.objects.all()
        for payment in payments:
            credit_card = payment.credit_card
            credit_card.delete()
            payment.delete()
        trolley_groups = TrolleyList.objects.all()
        for trolley_group in trolley_groups:
            trolley_group.delete()
        trolleys = Trolley.objects.all()
        for trolley in trolleys:
            trolley.delete()
        products = ProductItem.objects.all()
        LOGGER.info("Fetched {} product items".format(len(products)))
        for product in products:
            prices = product.prices.all()
            for price in prices:
                price.delete()
            product.delete()
        return JsonResponse({"result":"succeeded"}, status=200)
    else:
        return JsonResponse({"fail": "missing POST"}, status=400)
@csrf_exempt
def product_list(request):
    """
    List all product items, or create a new product.
    """
    if request.method == 'GET':
        products = ProductItem.objects.all()
        serializer = ProductItemSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code product item.
    """
    try:
        LOGGER.info("Fetching the product:{}".format(pk))
        productItem = ProductItem.objects.get(id=pk)
    except ProductItem.DoesNotExist:
        traceback.print_exc()
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductItemSerializer(productItem)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductItemSerializer(productItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        prices = productItem.prices.all()
        for price in prices:
            price.delete()
        productItem.delete()
        return HttpResponse(status=200)

@csrf_exempt
def trolley_list(request):
    """
    List all trolley, or create a new trolley.
    """
    if request.method == 'GET':
        trolleys = Trolley.objects.all()
        serializer = TrolleySerializer(trolleys, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrolleySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def trolley_detail(request, pk):
    """
    Retrieve, update or delete a trolley.
    """
    try:
        trolleyItem = Trolley.objects.get(id=pk)
    except Trolley.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrolleySerializer(trolleyItem)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrolleySerializer(trolleyItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        trolleyItem.delete()
        return HttpResponse(status=200)

@csrf_exempt
def trolley_group_list(request):
    """
    List all trolley group, or create a new trolley.
    """
    if request.method == 'GET':
        trolley_list = TrolleyList.objects.all()
        serializer = TrolleyListSerializer(trolley_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrolleyListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def trolley_group_detail(request, pk):
    """
    Retrieve, update or delete a trolley group.
    """
    try:
        trolley_box = TrolleyList.objects.get(id=pk)
    except TrolleyList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrolleyListSerializer(trolley_box)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrolleyListSerializer(trolley_box, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        trolley_box.delete()
        return HttpResponse(status=200)

@csrf_exempt
def credit_card_create(request):
    """
    List all trolley group, or create a new credit card object.
    """
    if request.method == 'GET':
        cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(cards, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreditCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def credit_card_detail(request, pk):
    """
    Retrieve, update or delete a credit card.
    """
    try:
        credit_card = CreditCard.objects.get(id=pk)
    except TrolleyList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CreditCardSerializer(credit_card)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CreditCardSerializer(credit_card, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        credit_card.delete()
        return HttpResponse(status=200)

@csrf_exempt
def transact_payment(request):
    """
    Submit a transaction for a payment
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse("Can't support {} for a transaction".format(request.method), status=400)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]