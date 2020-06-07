from django.contrib import admin

# Register your models here.
from .models import Article,Customers,Tag,Product,Order,Seasons,TotalTournament

admin.site.register(Article)

admin.site.register(Customers)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Tag)




admin.site.register(Seasons)

admin.site.register(TotalTournament)

