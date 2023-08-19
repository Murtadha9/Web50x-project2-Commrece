from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Listing, User,Bid ,Category,Comments


def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        'activeListings': activeListings,
        'categories': categories})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


#################################################################
def createListing(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        imageURL = request.POST['imageURL']
        price = request.POST['price']
        category = request.POST['category']
        categoryData = Category.objects.get(categoryName=category)
        currentUser = request.user
        bid = Bid(bid=price, user=currentUser)
        bid.save()
        newListing = Listing(title=title, description=description, imageURL=imageURL, price=bid,
                      owner=currentUser, category=categoryData, )
        newListing.save()
        return HttpResponseRedirect(reverse(index))
    
    elif request.method == "GET":
        return render(request, "auctions/create.html", {
            'categories': Category.objects.all()})
    
#################################################################
def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    comments = Comments.objects.all()
    currentUser = request.user
    isListInWatchlist = request.user in listingData.watchlist.all()
    return render(request, "auctions/listing.html", {
        'currentUser': currentUser,
        'listingData': listingData,
        'id': id,
        'isListInWatchlist': isListInWatchlist,
        'comments': comments}) 


#################################################################
def watchlist(request):
    currentUser = request.user
    activeListings = currentUser.listingWatchList.all()
    return render(request, 'auctions/watchlist.html', {
        'activeListings': activeListings,
        'currentUser': currentUser})

#################################################################
def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))



#################################################################
def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))


#################################################################
def comment(request, id):
    comment = request.POST['comment']
    usercomment = request.user
    listingData = Listing.objects.get(pk=id)
    newComment = Comments(message=comment,person=usercomment, listing=listingData)
    newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(id, )))



#################################################################
def addBid(request, id):
    newbid = request.POST['bid']
    listingData = Listing.objects.get(pk=id)
    if int(newbid) > listingData.price.bid:
        updateBid = Bid(user=request.user, bid=int(newbid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, 'auctions/listing.html', {
            "listingData": listingData,
            "message": "Successful Buy",
            "update": True})
    else:
        return render(request, 'auctions/listing.html', {
            "listingData": listingData,
            "message": "Failed Buy",
            "update": False})


#################################################################
def closeBid(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    currentUser = request.user
    isListInWatchlist = request.user in listingData.watchlist.all()
    comments = Comments.objects.all()
    return render(request, "auctions/listing.html", {
        'currentUser': currentUser,
        'listingData': listingData,
        'id': id,
        'isListInWatchlist': isListInWatchlist,
        'comments': comments,
        "message": "Bid has been closed"
    })


#################################################################
def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        'categories': categories,
    })

#################################################################
def displayCategory(request):
    if request.method == "POST":
        categoryForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryForm)
        activeListings = Listing.objects.filter(isActive=True, category=category)
        categories = Category.objects.all()
        return render(request, "auctions/index.html", {
            'activeListings': activeListings,
            'categories': categories})



#################################################################


























