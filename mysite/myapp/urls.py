from django.urls import path
from .import views
from .models import Product
urlpatterns = [
    path('', views.index,name='index'),
    path('product/<int:id>',views.detail,name='detail'),
]
