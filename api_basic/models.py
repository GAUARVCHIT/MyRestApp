from django.db import models

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=100)
    author= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 



# 
class Customers(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag,related_name='products_tag')

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = ( 
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customers = models.ForeignKey(
        Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name







# class TotalTournnament(models.Model):




class Seasons(models.Model):
    name=models.CharField(max_length=50,null=True)
    starting_date=models.DateField(auto_now_add=False,null=True)
    ending_date=models.DateField(auto_now_add=False,null=True)
    description=models.CharField(max_length=200,null=True,blank=True)











