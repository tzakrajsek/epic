from django.shortcuts import render

# Create your views here.

def index(request):
    # Render the template for our main page
    return render(request, 'index.html')
