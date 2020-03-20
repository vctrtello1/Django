from django.db import models

# Create your models here.


class Costumer (models.Model):
    name = models.CharField(max_length=60, null=True)
    phone = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=60, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag (models.Model):
    name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name


class Products (models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=60, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=60, null=True, choices=CATEGORY)
    description = models.CharField(max_length=60, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order (models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    costumer = models.ForeignKey(
        Costumer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Products, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=60, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
