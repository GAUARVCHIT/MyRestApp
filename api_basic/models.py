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

    def __str__(self):
        return self.name

class Organization(models.Model):
    name=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True,blank=True)

class Team(models.Model):
    name=models.CharField(max_length=50,null=True)
    short_name=models.CharField(max_length=10,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    organization=models.ManyToManyField(Organization,related_name='Organizations backing Teams')

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
    team=models.ForeignKey(Team,null=True, on_delete=models.SET_NULL)
    community=models.ManyToManyField(Community, related_name='People Roles in Community')
    mobile_no=models.IntegerField(max_length=10,blank=True,null=True)
    address=models.IntegerField(max_length=200,blank=True,null=True)
    # total_matches_played=models.IntegerField(max_length=10,null=True,blank=Ture)
    # total_kills=models.IntegerField(max_length=10,null=True,blank=True)
    # total_knockout=models.IntegerField(max_length=10,null=True,blank=True)
    # total_damage=models.IntegerField(max_length=10, null=True,blank=True)
    
    


class TotalTournament(models.Model):
    season= models.OneToOneField(Seasons, on_delete=models.CASCADE)
    teams_in_tournament= models.ManyToManyField(Team,related_name='Teams Participating in Tournaments')
    









