from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #######################################################
    path("create", views.createListing, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("closeBid/<int:id>", views.closeBid, name="closeBid"),
    path("categories/", views.categories, name="categories"),
    path("displayCategory/", views.displayCategory, name="displayCategory"),


]
