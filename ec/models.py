from django.db import models

# Create your models here.
class reg_Tbl(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=15)
    user=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)

class product_Tbl(models.Model):
    product_Name=models.CharField(max_length=100)
    img=models.FileField(upload_to="pictures")
    description=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.product_Name

class cart_Tbl(models.Model):
    fname=models.ForeignKey(reg_Tbl,on_delete=models.CASCADE)
    product_name=models.ForeignKey(product_Tbl,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    
class order_Tbl(models.Model):
    customer=models.ForeignKey(reg_Tbl,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    total_price=models.FloatField()
    status=models.CharField(max_length=50,default="Pending")
    
    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'
    
class orderItem_Tbl(models.Model):
    order=models.ForeignKey(order_Tbl,on_delete=models.CASCADE,related_name='item')
    product=models.ForeignKey(product_Tbl,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.FloatField()
    
    
    
