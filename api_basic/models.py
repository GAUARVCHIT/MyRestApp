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
    total_matches_played=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_kills=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_knockout=models.PositiveIntegerField(null=True,blank=True,default=0)
    total_damage=models.PositiveIntegerField( null=True,blank=True,default=0)


class TotalTournament(models.Model):
    season= models.ForeignKey(Seasons,null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    short_name=models.CharField(max_length=20,null=True,blank=True)
    teams= models.ManyToManyField(Teams,related_name='teams_participating_in_tournaments')
    description=models.CharField(max_length=200,blank=True,null=True)

    
    
    class Meta:
        verbose_name_plural = "TotalTournament"

    def __str__(self):
        return self.name


###################################################

class Days(models.Model):
    totalTournament=models.ManyToManyField(TotalTournament)
    date=models.DateField(auto_now_add=False,null=True)
    
    class Meta:
        verbose_name_plural = "Days"

    def __int__(self):
        return self.date

class Maps(models.Model):
    name=models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.name


class PointsTableType(models.Model):
    type=models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name_plural = "PointsTableType"

    def __str__(self):
        return self.type

class PointsTable(models.Model):
    pointsTableType=models.ForeignKey(PointsTableType,null=True,on_delete=models.SET_NULL)
    rank=models.IntegerField(null=True)
    placement_point=models.IntegerField(null=True)
    kill_points=models.IntegerField(null=True,default=1)

    class Meta:
        verbose_name_plural = "PointsTable"

    def __str__(self):
        return str(self.rank)


class Matches(models.Model):
    days=models.ForeignKey(Days,null=True,on_delete=models.SET_NULL)
    teams=models.ManyToManyField(Teams)
    match_stating_time=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    maps=models.ForeignKey(Maps,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.id)
    
class Results(models.Model):
    teams=models.ForeignKey(Teams,null=True,on_delete=models.CASCADE)
    points_table_type=models.ForeignKey(PointsTableType,null=True,on_delete=models.CASCADE)
    position= models.IntegerField(blank=True,null=True)
    kills=models.IntegerField(blank=True,null=True)
    matches=models.ForeignKey(Matches,null=True,on_delete=models.CASCADE)
    placement_point=models.IntegerField(null=True,default=0)
    kill_points=models.IntegerField(null=True,default=0)
    Total_points=models.IntegerField(null=True,default=0)
    class Meta:
        verbose_name_plural = "Results"

    def __str__(self):
        return str(self.matches)


###################################################






