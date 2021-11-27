from django.contrib import admin
from .models import MenuItem

# Register your models here.
admin.site.register(MenuItem)

admin.site.site_header = 'Sunset Restaurant Administration'
