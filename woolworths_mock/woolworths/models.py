##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################

from django.db import models
import logging

LOGGER = logging.getLogger(__name__)


class ProductPrice(models.Model):
    """
    The class is to define the Database Structure of product price
    """
    unit = models.CharField(max_length=50, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    original_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    save_price = models.FloatField(default=0)
    validate_condition = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def get_total_price(self, count):
        #type: (count) -> float
        """
        Get the total price for the input count
        :param count (float): input count
        :return (float): the total price
        """
        if self.discount:
            return self.discount * self.original_price * count
        elif self.save_price:
            return (self.original_price - self.save_price) * count
        else:
            return self.original_price * count


class ProductItem(models.Model):
    """
    The class is to define the Database Structure of product item
    """
    created = models.DateTimeField(auto_now_add=True)
    product_id = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    prices = models.ManyToManyField(ProductPrice, null=True)
    categories = models.CharField(max_length=100, blank=True, default='')
    expire_date = models.DateTimeField(blank=True, null=True)
    produce_date = models.DateTimeField(blank=True, null=True)
    product_photo_location = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['created']

    def get_unit_price(self, unit):
        # type: (unit)->ProductPrice
        """
        Fetch the ProductPrice according to input unit
        :param unit: the accepted unit name: such as "1kg" "each" "package" etc.
        :return: the corresponding price object
        """
        for price in self.prices.all():
            if price.unit == unit:
                return price
        return self.prices.all()[0]

class Trolley(models.Model):
    """
    The class is to define the database structure of trolley item
    """
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=1)
    notes = models.CharField(max_length=50, blank=True, default='')
    checked = models.BooleanField(default=True)
    selected_unit = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def get_itemtotal_price(self):
        #type: ()->float
        """
        Calculate the total price for a single trolley item
        :return (float): total price value
        """
        price = self.product.get_unit_price(self.selected_unit)
        return price.get_total_price(self.count)


class TrolleyList(models.Model):
    """
    The class is to define a trolley item list for paying
    """
    created = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Trolley, null=True)
    name = models.CharField(max_length=50, blank=True, default='temp')
    notes = models.CharField(max_length=50, blank=True, default='')

    def get_checked_items(self):
        #type: () -> list
        """
        Fetch the checked items
        :return (list): checked items or empty array if no checked item
        """
        selected_items = []
        for item in self.items.all():
            if item.checked:
                selected_items.append(item)
        return selected_items

    def get_total_price(self):
        #type: ()->float
        """
        Calculate the total price for checked item in the trolley
        :return(float): the total price
        """
        total_price = 0
        for item in self.get_checked_items():
            total_price += item.get_itemtotal_price()
        return total_price


class CreditCard(models.Model):
    """
    The class is to define a credit card instance for payment
    """
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, blank=False)
    cardnumber = models.CharField(max_length=100, blank=False)
    expirary_date = models.DateTimeField(blank=False, null=False)
    cvc = models.CharField(max_length=20, blank=False, default='')

    def check_validate(self):
        """
        Check if the credit card is validated
        :return (bool): true if validated or false
        """
        return True

    def complete_transaction(self, total_cost):
        #type: (total_cost) -> boolean
        """
        complete transaction for the credit card payment
        :param total_cost (float): the cost number for this payment
        :return (boolean): true if succeeded or false
        """
        return True


class Payment(models.Model):
    """
    The class is to complete the payment for trolley items
    """
    created = models.DateTimeField(auto_now_add=True)
    trolley = models.ForeignKey(TrolleyList, on_delete=models.CASCADE, null=True)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']

    def do_payment(self):
        """
        Complete the trasaction for the payment
        :return:
        """
        total_price = self.trolley.get_total_price()
        if(self.credit_card.check_validate() and self.credit_card.complete_transaction(total_price)):
            return True
        else:
            return False
