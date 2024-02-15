from django.shortcuts import render
from .models import Product
from django.conf import settings
import stripe
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    stripe_publisheable_key= settings.STRIPE_PUBLISHEABLE_KEY
    return render(request, 'myapp/detail.html',{'product':product, 'stripe_publisheable_key':stripe_publisheable_key})





