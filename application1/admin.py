from django.contrib import admin
from application1.models import product_management

@admin.register(product_management,product_management_admin)
class product_management_admin(admin.ModelAdmin):
    list_display=['pid','pname','account','adress','product']
# Register your models here.
