from django.shortcuts import render

from .models import Category, Product

def index(request):
    return render(request, 'kraving/index.html')

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'kraving/index.html', {'products': products})


# Create your views here.
# def Search(request):
#     pass

# def Account(request):
#     pass

# def Cart(request):
#     pass

# def HomeView(request):
#     pass
