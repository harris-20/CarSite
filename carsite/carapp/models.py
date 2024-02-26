from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class CarType(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=10, decimal_places=4)
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)
    product_description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.car_name


class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
        ('C', 'Chatham'),
        ('T', 'Toronto'),
        ('WA', 'Waterloo')
    ]

    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='C')
    interested_in = models.ManyToManyField(CarType)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    def __str__(self):
        return self.username


class OrderVehicle(models.Model):
    ORDER_STATUS_CHOICES = [
            (0, 'Cancelled'),
            (1, 'Placed'),
            (2, 'Shipped'),
            (3, 'Delivered'),
        ]

    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField(default=1)
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1)
    last_updated = models.DateTimeField(auto_now=True)

    def total_price(self):
        return self.quantity_ordered * self.vehicle.car_price

    def __str__(self):
        return f"Order #{self.id} - {self.vehicle.car_name} ({self.quantity_ordered} units)"

class GroupMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    semester = models.IntegerField(default=3)
    personal_page = models.URLField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering= ['first_name']