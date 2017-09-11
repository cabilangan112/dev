from django.contrib import admin
import models

from .models import Restaurant
class RestaurantAdmin(admin.ModelAdmin):
	fieldset = [("res Restaurant", {"field":["name","street","number","city","zipCode","country","telephone","url","user","date"]})
	]
	
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(models.Dish)
admin.site.register(models.RestaurantReview)