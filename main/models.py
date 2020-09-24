from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    TYPE = [
        ('Paid Review', 'Paid Review'),
        ('Advertise', 'Advertise'),
        ('Customer Review', 'Customer Review')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(choices=TYPE, max_length=50, blank=True)
    item_name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    thumbnail = models.ImageField(
        upload_to='postthumb', max_length=250, default='postthumb/default.jpg')
    address = models.CharField(max_length=100, blank=True)
    price = models.FloatField(max_length=50, blank=True)
    restaurant_name = models.CharField(max_length=250, blank=True)
    rating = models.FloatField(max_length=50, blank=True)
    up_vote = models.ManyToManyField(User, related_name='up_vote', blank=True)
    down_vote = models.ManyToManyField(
        User, related_name='down_vote', blank=True)
    views = models.IntegerField(default=0)

    def total_up_votes(self):
        return self.up_vote.count()

    def total_down_votes(self):
        return self.down_vote.count()
    
    def __str__(self):
        return self.user.username


class PostGallery(models.Model):
    img_url = models.ImageField(upload_to='post')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Restaurant(models.Model):
    TYPE = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=250, blank=True)
    booking_system = models.CharField(choices=TYPE, max_length=50, blank=True)
    avatar = models.ImageField(
        upload_to='restaurant', max_length=250, default='restaurant/default.jpg')
    address = models.CharField(max_length=100, blank=True)
    about_us= models.CharField(max_length=250, blank=True)
    discount= models.FloatField(max_length=50, blank=True)
    time_schedule = models.CharField(max_length=50, blank=True)
    
    
    def __str__(self):
        return self.name

class ResturantGallery(models.Model):
    img_url = models.ImageField(upload_to='resturant')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

# class RestaurantAdmin(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)


class FoodItem(models.Model):
     TYPE = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
     name = models.CharField(max_length=250, blank=True)
     avatar = models.ImageField(
         upload_to='food', max_length=250, default='food/default.jpg')
     description = models.CharField(max_length=250, blank=True)
     address = models.CharField(max_length=100, blank=True)
     price = models.FloatField(max_length=50, blank=True)
     discount= models.FloatField(max_length=50, blank=True)
     quantity = models.IntegerField(max_length=50, blank=True)
     food_available = models.CharField(choices=TYPE, max_length=50, blank=True)

class PostComent(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class FoodOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=50, blank=True)
    vat = models.FloatField(max_length=50, blank=True)
    Delivery_charge = models.FloatField(max_length=50, blank=True)
    total_price = models.FloatField(max_length=50, blank=True)
