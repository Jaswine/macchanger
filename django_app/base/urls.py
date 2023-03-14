from  django.urls import path
from . import views

app_name = 'base';

urlpatterns = [
   path("company/<str:slug>/", views.showCompany, name="company"),
   
   path("home", views.home, name="home"),
   path("create", views.create, name="create"),
   path("create-social-media/<str:slug>/", views.createCompanySocialMedia, name="createCompanySocialMedia"),
   path("constructor/<str:slug>/", views.constructor, name="constructor"),
   path("company/<str:slug>/delete", views.cardDelete, name="company-delete"),
]