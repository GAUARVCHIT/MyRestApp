
from django.urls import path
from .views import article_list,article_details,ArticleAPIView,ArticleDetails,customers_list,tag_list,product_list,order_list

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:pk>',ArticleDetails.as_view()),
    path('',article_list ),
    # path('detail/<int:pk>',article_details)
    path('customers/',customers_list),
    path('tag/',tag_list),
    path('product/',product_list),
    path('order/',order_list),
]