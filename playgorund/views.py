from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.

def home(request):
    # query_set = Product.objects.all()
    # query_set = Product.objects.count()
    # try:
    #     query_set = Product.objects.get(id= 0)
    # except ObjectDoesNotExist:
    #     pass
    query_set = Product.objects.filter(id= 0).first()
    print(query_set)
    return render(request, 'home.html')