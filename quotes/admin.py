from django.contrib import admin

# Register your models here.

from .models import Stock
# register db:
admin.site.register(Stock)


