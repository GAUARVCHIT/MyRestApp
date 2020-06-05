from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializers= ArticleSerializers(articles,many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers= ArticleSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)

        except Article.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, pk):
        article= self.get_object(pk)
        serializers= ArticleSerializers(article)
        return Response(serializers.data)

    def put(self, request, pk):
        article= self.get_object(pk)
        serializers=ArticleSerializers(article,data=request.data )

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article= self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializers= ArticleSerializers(articles,many=True)
        return Response(serializers.data)
    
    elif request.method== 'POST':
        serializers= ArticleSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def article_details(request,pk):
    try:
        article=Article.objects.get(id=pk)

    except Article.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializers= ArticleSerializers(article)
        return Response(serializers.data)

    elif request.method== 'PUT':
        serializers=ArticleSerializers(article,data=request.data )

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method== 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












@api_view(['GET','POST'])
def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializers= ProductSerializers(products,many=True)
        return Response(serializers.data)
    
    elif request.method== 'POST':
        serializers= ProductSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','POST'])
def customers_list(request):

    if request.method == 'GET':
        customers = Customers.objects.all()
        serializers= CustomersSerializers(customers,many=True)
        return Response(serializers.data)
    
    elif request.method== 'POST':
        serializers= CustomersSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','POST'])
def tag_list(request):

    if request.method == 'GET':
        tags = Tag.objects.all()
        serializers= TagSerializers(tags,many=True)
        return Response(serializers.data)
    
    elif request.method== 'POST':
        serializers= TagSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   



@api_view(['GET','POST'])
def order_list(request):

    if request.method == 'GET':
        orders = Order.objects.all()
        serializers= OrderSerializers(orders,many=True)
        return Response(serializers.data)
    
    elif request.method== 'POST':
        serializers= OrderSerializers(data= request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
