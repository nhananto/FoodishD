from django.contrib import admin
from .models import *



admin.site.register(Post)
admin.site.register(PostGallery)
admin.site.register(Restaurant)
admin.site.register(ResturantGallery)
admin.site.register(RestaurantAdmin)
admin.site.register(FoodItem)
admin.site.register(PostComment)
admin.site.register(FoodOrder)

