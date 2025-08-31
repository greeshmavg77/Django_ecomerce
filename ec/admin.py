from itertools import product
from .models import cart_Tbl, product_Tbl, reg_Tbl
from django.contrib import admin

# Register your models here.
admin.site.register(reg_Tbl)
admin.site.register(product_Tbl)
admin.site.register(cart_Tbl)
