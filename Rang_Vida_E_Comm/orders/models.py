from django.db import models
from django.contrib.auth.models import User
from Products.models import Category, Product


# Create your models here.
class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES  =(
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    #this connects the Order database model to the user model from django.contrib.auth.models
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    phone = models.IntegerField()
    place = models.CharField(max_length=255, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount= models.IntegerField(blank=True, null=True)

    status  = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)
   
   

    class Meta:
        ordering = ('-created_at',)
        #minus means descending order

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount

        return 0
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)


    def get_total_price(self):
        return self.price


