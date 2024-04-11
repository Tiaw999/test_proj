#######################################################
# Views
# Tia and Zach
# 04-09-24
#######################################################

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Exhibit, Media, Play
from .forms import DataForm
from random import shuffle

# Create your views here.


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    exhibits = Exhibit.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q))
    media = Media.objects.all()
    exhibit_count = exhibits.count()
    context = {'exhibits': exhibits, 'media': media, 'exhibit_count': exhibit_count}
    return render(request, 'core/home.html', context)

def exhibitentry_test(request):
    images_info = [
        {'image_url': 'path/to/your/first/image.jpg', 'title': 'First Title', 'subtitle': 'First Subtitle'},
        {'image_url': 'path/to/your/second/image.jpg', 'title': 'Second Title', 'subtitle': 'Second Subtitle'},
        {'image_url': 'path/to/your/third/image.jpg', 'title': 'Third Title', 'subtitle': 'Third Subtitle'},
    ]
    return render(request, 'exhibitEntry_test.html', {'images_info': images_info})

def exhibitlist(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    exhibits = Exhibit.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q))
    media = Media.objects.all()
    exhibit_count = exhibits.count()
    context = {'exhibits': exhibits, 'media': media, 'exhibit_count': exhibit_count}
    return render(request, 'core/exhibitlist.html', context)

def exhibit(request, pk):
    exhibit_instance = Exhibit.objects.get(id=pk)
    form = DataForm(initial={'exhibit': exhibit_instance})  # Set the initial value for the exhibit field

    play = Play.objects.all()  # Assuming you want to list all play types in the form

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            # Assuming your form saves a model that links plays to the exhibit
            form.save()
            return redirect('exhibit', pk=pk)  # Redirect to the same page to show a success message or similar

    context = {'exhibit': exhibit_instance, 'form': form, 'play': play}
    return render(request, 'core/exhibit.html', context)

def sendData(request):
    play = Play.objects.all()
    play = list(play)
    shuffle(play)
    form = DataForm()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibit', pk=form.cleaned_data['exhibit'].id)
    context = {'form': form, 'play': play}
    return render(request, 'core/exhibit.html', context)


def playInfo(request):
    return render(request, 'core/play_info.html')
