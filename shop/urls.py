
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('history/',views.history),
    path('productview/<int:prodid>',views.productview),
    path('contact/',views.contact)
]
