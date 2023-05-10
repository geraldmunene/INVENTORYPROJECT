from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('BODY WORKS', 'BODY WORKS'),
    ('PARCO RABBANE', 'PARCO RABBANE'),
    ('CREATION', 'CREATION'),
    ('ESCADA', 'ESCADA'),
    ('RALPH LAUREEN', 'RALPH LAUREEN'),
    ('DUNHILL', 'DUNHILL'),
    ('DIOR', 'DIOR'),
    ('RIHANNA', 'RIHANNA'),    
    ('VICTORIA SECRET', 'VICTORIA SECRET'),    
    ('SWEET', 'SWEET'),    
    ('CAROLINA HERERRA', 'CAROLINA HERERRA'),    
    ('CALVIN KLEIN', 'CALVIN KLEIN'),    
    ('B.SPEARS', 'B.SPEARS'),  
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Product'


    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'


