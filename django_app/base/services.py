from .models import *

def get_product(slug):
   return  Company.objects.get(slug = slug)

def get_company_icons(companyModel):
   return CompanySocialMedia.objects.get(contact=companyModel)

def get_all_products():
   return Company.objects.all()
   