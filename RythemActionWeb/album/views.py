from django.shortcuts import render

# Create your views here.
from .models import Image

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'album/showall.html', context)
