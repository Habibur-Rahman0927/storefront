"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from pprint import pprint

# router = DefaultRouter()
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# pprint(router.urls)
# urlpatterns = [
#     path('', include(router.urls)), 
#     path('product/', views.ProductList.as_view()),
#     path('product/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/<int:pk>/', views.collection_details, name='collection-detail'),
# ]
urlpatterns = [
    path(r'', include(router.urls)), 
    path(r'', include(products_router.urls)), 
]