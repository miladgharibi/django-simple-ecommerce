from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

def productImage(instance, filename):
    return f'{instance.title}-{instance.date}/{filename}'

class ProductModel(models.Model):
    title           = models.CharField(max_length=255, blank=False)
    description     = models.TextField()
    price           = models.IntegerField(blank=False)
    discount_price  = models.IntegerField(null=True,blank=True)
    date            = models.DateTimeField(auto_now_add=True)
    image           = models.ImageField(upload_to=productImage)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-date']


    def get_absolute_url(self):
        return f"/shop/{self.id}/"
    

    def get_price(self):
        if self.discount_price:
            return self.discount_price
        else:
            return self.price



class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.user.username}: {self.quantity} of {self.product.title}"


    def get_total_item_price(self):
        return self.quantity * self.product.price


    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(OrderProduct)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


    def get_total(self):
        price = 0
        for order_item in self.orders.all():
            price += order_item.get_final_price()
        
        return price