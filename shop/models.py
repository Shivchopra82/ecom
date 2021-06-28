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