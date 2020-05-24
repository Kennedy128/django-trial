from django.shortcuts import render
from .models import Image, Category, Location

def index(request):
    '''
    Displays home page
    '''
    title = "Gallery"
    images = Image.display_all_images()
    return render(request, "index.html", {"title": title, "images":images})

def image_search(request):
    '''
    Displays the search results page
    '''

    title = "Search results"
    if 'category' in request.GET and request.GET["category"]:
        searched_category = request.GET.get("category")
        searched_images = Image.search_image(searched_category)
        message = f"{searched_category}"
        print("*"*80)
        print(searched_images)
        print(searched_category)
        print(len(searched_images))
        
        return render(request, 'search.html', {"message":message, "searched_images": searched_images,"title": title})


    else:
        message = "You haven't searched for anything"
        return render(request, 'search.html', {"message":message,"title": title})

def locations_display(request):
    '''
    Function to display the locations
    '''
    title = "Locations"
    locations = Location.display_all_locations()


    return render(request, 'location.html', { "title": title, "locations" :locations})

def location_images(request,location):
    '''
    Function to display images per location
    '''
    location_images = Image.filter_by_location(location)

    return render(request, 'location.html', { "location_images" :location_images})

# Create your views here.
