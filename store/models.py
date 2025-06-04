from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.templatetags.static import static
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
     return self.name or f"Customer {self.id}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    digital = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images',null=True,blank=True)
    
    def __str__(self):
        return self.name
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = static('images/images.jpg')
        return url
    
PAYMENT_CHOICES = [
    ('COD', 'Cash on Delivery'),
    ('Bkash', 'Bkash'),
    ]
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200,null=True)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    class Meta:
        ordering = ('-date_ordered',)
    
    def __str__(self):
      return f"Order #{self.id} by {self.customer.name}"
  
    @property
    def get_cart_items(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    @property
    def get_cart_total(self):
        return sum(item.quantity * item.product.price for item in self.orderitem_set.all())


    

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order   = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)  
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else 'Unknown Product'}"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} ({self.zipcode})"
    
 