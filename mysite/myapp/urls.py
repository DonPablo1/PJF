from django.urls import path
from .import views
from .models import Product
urlpatterns = [
    path('', views.index,name='index'),
    path('product/<int:id>',views.detail,name='detail'),
    path('success/',views.payment_success_view,name='success'),
    path('failed/',views.payment_failed_view,name='failed'),
]
