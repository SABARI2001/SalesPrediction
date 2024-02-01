from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = (
        'Item_Identifier',
        'Item_Weight',
        'Item_Fat_Content',
        'Item_Visibility',
        'Item_Type',
        'Item_MRP',
        'Outlet_Identifier',
        'Outlet_Establishment_Year',
        'Outlet_Location_Type',
        'Outlet_Type',
        'Item_Outlet_Sales',
        'source',
    )

admin.site.register(Data, DataAdmin)