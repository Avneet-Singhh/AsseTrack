from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY=(
    ('Stationary','Stationary'),
    ('Grocery','Grocery'),
    ('Electronics','Electronics'),
)

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, null=False, blank=False)
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=25, choices=CATEGORY, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name='products')  # Use related_name to avoid conflicts
    PRODUCT_STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available'),
    )
    status = models.CharField(max_length=15, choices=PRODUCT_STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        return f'{self.name}-{self.quantity}'

    
class Order(models.Model):
    product= models.ForeignKey("Product", on_delete=models.CASCADE, null=False)
    staff= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    order_quantity= models.PositiveIntegerField(null=False)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.product} ordered by {self.staff.username}'    