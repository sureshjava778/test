from django.contrib import admin
from vsapp.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name']    
admin.site.register(Customer)
