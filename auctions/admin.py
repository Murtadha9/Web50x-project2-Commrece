from django.contrib import admin

from .models import Listing, User,Bid ,Category,Comments

admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Comments)
