from rest_framework import serializers
from .models import *



class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','title','author']

class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    tag= serializers.StringRelatedField(many=True)

    class Meta:
        model=Product
        fields='__all__'

class TagSerializers(serializers.ModelSerializer):
    products_tag = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model=Tag
        fields=('id','name','products_tag')

class OrderSerializers(serializers.ModelSerializer):
    customers= serializers.StringRelatedField()

    class Meta:
        model=Order
        fields='__all__'