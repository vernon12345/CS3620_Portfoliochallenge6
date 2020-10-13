from django.contrib import admin#imports
from .models import Hobby#imports
from .models import portfolio#imports
from .models import contact#imports

# Register your models here.
admin.site.register(Hobby)#registering model
admin.site.register(portfolio)#registering model
admin.site.register(contact)#registering model