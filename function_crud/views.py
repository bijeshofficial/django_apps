from django.shortcuts import redirect, render
from .models import Musician, Album
from .forms import MusicianCreateForm, AlbumCreateForm


# Create your views here.


def index(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    context = {
        'musicians': musicians,
        'albums': albums
    }
    return render(request, 'function_crud/function_index.html', context)


def create_musician(request):
    if request.method == "POST":
        form = MusicianCreateForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('function_index')
    else:
        form = MusicianCreateForm()
        context = {
            "form": form
        }
        return render(request, 'function_crud/create_musician.html', context)


def create_album(request):
    if request.method == "POST":
        form = AlbumCreateForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('function_index')

    form = AlbumCreateForm()
    context = {
        "form": form
    }
    return render(request, 'function_crud/create_album.html', context)


def update_musician(request, id):
    musician = Musician.objects.get(pk=id)
    if request.method == "POST":
        form = MusicianCreateForm(request.POST, instance=musician)
        if form.is_valid:
            form.save()
        return redirect('function_index')
    form = MusicianCreateForm(instance=musician)
    context = {
        'form': form
    }
    return render(request, 'function_crud/create_musician.html', context)


def update_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == "POST":
        form = AlbumCreateForm(request.POST, instance=album)
        if form.is_valid:
            form.save()
        return redirect('function_index')
    form = AlbumCreateForm(instance=album)
    context = {
        'form': form
    }
    return render(request, 'function_crud/create_album.html', context)


def delete_musician(request, id):
    musician = Musician.objects.get(pk=id)
    if request.method == "POST":
        musician.delete()
        return redirect('function_index')
    return render(request, 'function_crud/confirm_delete.html')


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == "POST":
        album.delete()
        return redirect('function_index')
    return render(request, 'function_crud/confirm_delete.html')
