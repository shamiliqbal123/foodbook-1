from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cact_img = models.ImageField(upload_to='cat_image',blank=True,null=True)
    trash = models.BooleanField(default=False)


    def __str__(self):
        return self.cat_name

class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_image = models.ImageField(upload_to='menu_images/')
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    today_special=models.BooleanField(default=False)
    popular_item=models.BooleanField(default=False)
    offer_item = models.BooleanField(default=False)


    def __str__(self):
        return self.item_name

class OrderStatus(models.Model):
    order_status=models.CharField(max_length=50)
    order_time=models.DateTimeField(auto_now=True)
    total=models.IntegerField()
    trash=models.BooleanField(default=False)
    def __str__(self) :
        return self.order_status
    @property
    def OrderItemss(self):
        return self.orderitems_set.all()

class OrderItems(models.Model):
    item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    item_quantity=models.IntegerField()
    item_total=models.IntegerField()
    order=models.ForeignKey(OrderStatus,on_delete=models.CASCADE)
    def __str__(self):
        return self.item_total

