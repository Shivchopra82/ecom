from django.db import models

class product(models.Model):
    prod_id = models.AutoField
    prod_name = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=3000)
    prod_pub_date = models.DateField()
    prod_price = models.IntegerField(default=0)
    prod_category = models.CharField(max_length=50, default="")
    prod_subcategory = models.CharField(max_length=50, default="")
    prod_img = models.ImageField(upload_to="shop/images", default="")
    prod_company = models.CharField(max_length=50, default="made in china")

    def __str__(self):
        return self.prod_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=40, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."


