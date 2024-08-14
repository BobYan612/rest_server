##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################
import logging
from rest_framework import serializers
from .models import ProductPrice, ProductItem, Trolley, CreditCard, TrolleyList, Payment
from django.contrib.auth.models import Group, User

LOGGER = logging.getLogger(__name__)
class ProductPriceSerializer(serializers.ModelSerializer):
    """
    The class is used to serialize the price object
    """
    class Meta:
        model = ProductPrice
        fields = ['id', 'unit', 'original_price', 'discount', 'save_price', 'validate_condition']


class ProductItemSerializer(serializers.ModelSerializer):
    """
    The class is used to serialize the product item object
    """
    prices = ProductPriceSerializer(many=True)
    expire_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    produce_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    def get_or_create_product_prices(self, prices):
        #type: (prices) -> list
        """
        The method is used to fetch or create a Price object
        :param prices (list): the json list of price definition
        :return (list): the price object id list
        """
        price_ids = []
        for price in prices:
            price_instance, created = ProductPrice.objects.get_or_create(pk=price.get('id'), defaults=price)
            price_ids.append(price_instance.pk)
        return price_ids

    def create_or_update_prices(self, prices):
        #type: (prices) -> list
        """
        The method is used to create or update the price objects
        :param prices(list): The list of price definition
        :return (list): the list of price object id.
        """
        price_ids = []
        for price in prices:
            price_instance, created = ProductPrice.objects.update_or_create(pk=price.get('id'), defaults=price)
            price_ids.append(price_instance.pk)
        return price_ids

    def create(self, validated_data):
        #type: (validated_date)->ProductItem
        """
        Create a new product item including its price object(s)
        :param validated_data (json): the definition of product item
        for example:
        {
            "product_id": "48211",
            "name" : "Mainland Cheese Colby",
            "description" : "Block 1kg  $1.35 / 100g",
            "prices" : [
               {
                  "original_price" : "17.39",
                  "save_price" : "3.89",
                  "unit" : "1kg"
               }
            ],
            "categories" : "Fridge & Deli/Cheese/Block Cheese",
            "product_photo_location" : "images/2010/48211.jpg"
        }
        :return (ProductItem): the object of ProductItem
        """
        prices = validated_data.pop('prices', [])
        procut = ProductItem.objects.create(**validated_data)
        procut.prices.set(self.get_or_create_product_prices(prices))
        return procut

    def update(self, instance, validated_data):
        #type: (instance, validated_date)->ProductItem
        """
        Update the existing product item.
        :param instance (ProductItem): the instance of ProductItem
        :param validated_data(json): The new value of the product item
        :return (ProductItem): the instance of ProductItem with new value
        """
        prices = validated_data.pop('prices', [])
        instance.prices.set(self.create_or_update_prices(prices))
        fields = ['product_id', 'name', 'categories', 'expire_date', 'produce_date', 'product_photo_location', 'description']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance

    class Meta:
        model = ProductItem
        fields = ['id', "created", 'product_id', 'name', 'prices', 'categories', 'expire_date', 'produce_date', 'product_photo_location', 'description']


class CreditCardSerializer(serializers.ModelSerializer):
    expirary_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=True)
    class Meta:
        model = CreditCard
        fields = "__all__"


class TrolleySerializer(serializers.ModelSerializer):
    """
    The class is used to serialize the trolley object
    """
    # product = ProductItemSerializer(many=False)

    class Meta:
        model = Trolley
        fields = "__all__"

    def create(self, validated_data):
        LOGGER.info(validated_data)
        product = validated_data.get("product")
        try:
            instance = Trolley.objects.get(product=product)
            instance.count = validated_data.get("count", instance.count)
            instance.notes = validated_data.get("notes", instance.count)
            instance.checked = validated_data.get("checked", instance.checked)
        except Trolley.DoesNotExist:
            instance = Trolley.objects.create(**validated_data)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.count = validated_data.get("count", instance.count)
        instance.notes = validated_data.get("notes", instance.count)
        if instance.count == 0:
            instance.delete()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class TrolleyListSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True,  read_only=False, queryset=Trolley.objects.all())

    class Meta:
        model = TrolleyList
        fields = "__all__"

    # def get_trolley_items(self, trolley_items):
    #     #type: (trolley_items) -> list
    #     """
    #     The method is used to fetch trolley item object
    #     :param trolley_items (list): the json list of trolley item definition
    #     :return (list): the trolley object id list
    #     """
    #     item_ids = []
    #     for item in trolley_items:
    #         instance= Trolley.objects.get(pk=item)
    #         item_ids.append(instance.pk)
    #     return item_ids
    #
    # def update_trolley_item(self, trolley_items):
    #     #type: (prices) -> list
    #     """
    #     The method is used to create or update the trolley items
    #     :param trolley_items(list): The list of trolley definition
    #     :return (list): the list of trolley object id.
    #     """
    #     items = []
    #     for item in trolley_items:
    #         instance, created = Trolley.objects.update(pk=item)
    #         items.append(instance.pk)
    #     return items
    #
    # def create(self, validated_data):
    #     #type: (validated_date)->TrolleyList
    #     """
    #     Create a new trolley list including its trolley items
    #     :param validated_data (json): the definition of trolley list
    #     :return (ProductItem): the object of ProductItem
    #     """
    #     items = validated_data.pop('items', [])
    #     LOGGER.info("items are {}".format(items))
    #     procut = TrolleyList.objects.create(**validated_data)
    #     procut.items.set(self.get_trolley_items(items))
    #     return procut
    #
    # def update(self, instance, validated_data):
    #     #type: (instance, validated_date)->ProductItem
    #     """
    #     Update the existing trolley list.
    #     :param instance (ProductItem): the instance of ProductItem
    #     :param validated_data(json): The new value of the product item
    #     :return (ProductItem): the instance of ProductItem with new value
    #     """
    #     items = validated_data.pop('items', [])
    #     instance.items.set(self.update_trolley_item(items))
    #     fields = ['notes', 'name']
    #     for field in fields:
    #         try:
    #             setattr(instance, field, validated_data[field])
    #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
    #             pass
    #     instance.save()
    #     return instance

class PaymentSerializer(serializers.ModelSerializer):
    credit_card = CreditCardSerializer(many=False, read_only=False)
    trolley = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=TrolleyList.objects.all())
    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validated_data):
        #type: (validated_date)->TrolleyList
        """
        Create a new transaction, return instance if true or return None
        :param validated_data (json): the definition of transaction
        :return (Payment): the object of payment
        """
        card = validated_data.pop("credit_card")
        card_instance = CreditCard.objects.create(**card)
        validated_data['credit_card'] = card_instance
        payment = Payment.objects.create(**validated_data)
        if(payment.do_payment()):
            return payment
        else:
            payment.delete()
            return None


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']