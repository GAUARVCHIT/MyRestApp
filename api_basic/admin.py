from django.contrib import admin

# Register your models here.
from .models import Article,Customers,Tag,Product,Order

admin.site.register(Article)

admin.site.register(Customers)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Tag)