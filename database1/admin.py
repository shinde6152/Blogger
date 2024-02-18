from django.contrib import admin
from .models.khanda import khanda,country,Blog,fieldtype,favourite
from .models.countries import belize
from .models.contact import contacts

# Register your models here.

class description(admin.ModelAdmin):
    list_display=['heading','description','image','heading2','description2','image2']

class blog_desc(admin.ModelAdmin):
    list_display=['khanda','country','field_type','favourite_type','heading','description','image11','heading2','description2','image22']

class contact_data(admin.ModelAdmin):
    list_display=['name','email','subject','message']


admin.site.register(khanda)
admin.site.register(country)
admin.site.register(fieldtype)
admin.site.register(favourite)
admin.site.register(belize,description)
admin.site.register(Blog,blog_desc)
admin.site.register(contacts,contact_data)