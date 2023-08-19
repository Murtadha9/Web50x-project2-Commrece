from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

################################################
class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

################################################

class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

################################################
class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    imageURL = models.CharField(max_length=4000 , blank=True, null=True)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="pricebid")
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey( Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listingWatchList")
    
    def __str__(self):
        return self.title

################################################
class Comments(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="personcomment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listingcomment")
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.person} comments on {self.listing}"