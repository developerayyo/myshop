from django.urls import path
from .import views


app_name = 'shop'
urlpatterns = [
    path('contact-us/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
]
