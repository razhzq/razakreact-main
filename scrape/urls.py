from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.NewsListCreate.as_view()),
    path('price/', views.IndexPriceCreate.as_view())
]