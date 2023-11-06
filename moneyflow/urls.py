from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name="index"),
    path('account/', views.accounts, name="account"),
    path('document/', views.documents, name="document"),
]
