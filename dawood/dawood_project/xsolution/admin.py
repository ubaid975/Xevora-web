from django.contrib import admin
from xsolution.models import contact

# Register your models here.
@admin.register(contact)
class contact(admin.ModelAdmin):
    
    list_display=['help','industry','first_name','last_name','phone','email','company','message']
