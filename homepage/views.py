from django.shortcuts import render

# Create your views here.

# This function returns the homepage.
def index(request):
    return render(request, 'homepage/index.html')
