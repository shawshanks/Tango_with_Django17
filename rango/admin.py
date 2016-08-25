from django.contrib import admin

# username = yang
# password = 1234yang_huan

from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)