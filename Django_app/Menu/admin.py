from django.contrib import admin
from .models import Restaurant,Food

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')

admin.site.register(Food)
admin.site.register(Restaurant)