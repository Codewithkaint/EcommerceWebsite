from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=300)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=1000,default="")
    price=models.IntegerField(default=200)
    desc=models.CharField(max_length=1000)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=20)
    number=models.CharField(max_length=12,default="")
    item=models.CharField(max_length=100,default="")
    query=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.email
    




class Orders(models.Model):
  
    order_id=models.AutoField(primary_key=True)
    json=models.CharField(max_length=3000,default="")
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    name=models.CharField(max_length=100 )
    order=models.CharField(max_length=100)
    add1=models.CharField(max_length=100)
    add2=models.CharField(max_length=100)
    prices=models.CharField(max_length=100,default="")
    

    
    def __str__(self):
        return self.name

class Tracker(models.Model):
    updated_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    new_desc=models.CharField(max_length=300)
    time=models.DateField(auto_now_add=True)



    def __str__(self):
        return self.new_desc[0:8]+"..."



