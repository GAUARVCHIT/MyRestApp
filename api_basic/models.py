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



class Seasons(models.Model):
    name=models.CharField(max_length=50,null=True)
    starting_date=models.DateField(auto_now_add=False,null=True)
    ending_date=models.DateField(auto_now_add=False,null=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Seasons"

    def __str__(self):
        return self.name

class Organizations(models.Model):
    name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name

class Teams(models.Model):
    name=models.CharField(max_length=50,null=True)
    short_name=models.CharField(max_length=10,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    organizations=models.ManyToManyField(Organizations,related_name='organizations_backing_teams')

    class Meta:
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.short_name

class Community(models.Model):
    role=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=200,null=True)


class Peoples(models.Model):
    GENDER = ( 
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    name=models.CharField(max_length=50,null=True,blank=True)
    ingame_name=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=20,null=True,choices=GENDER)
    pubg_id=models.CharField(max_length=30,null=True,blank=True)
    team=models.ForeignKey(Teams,null=True, on_delete=models.SET_NULL)
    community=models.ManyToManyField(Community, related_name='peoples_roles_in_community')
    mobile_no=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    # total_matches_played=models.IntegerField(null=True,blank=Ture)
    # total_kills=models.IntegerField(null=True,blank=True)
    # total_knockout=models.IntegerField(null=True,blank=True)
    # total_damage=models.IntegerField( null=True,blank=True)
    

class TotalTournament(models.Model):
    season= models.OneToOneField(Seasons, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    short_name=models.CharField(max_length=20,null=True,blank=True)
    teams= models.ManyToManyField(Teams,related_name='teams_participating_in_tournaments')
    description=models.CharField(max_length=200,blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "TotalTournament"

    def __str__(self):
        return self.name








