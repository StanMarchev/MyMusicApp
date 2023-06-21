from django.shortcuts import render, redirect

from MyMusicApp.music.forms import ProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from MyMusicApp.music.models import Profile, Album


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    if not profile:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home-page')

        return render(request, 'home-no-profile.html', {'form': form})

    albums = Album.objects.all()
    return render(request, 'home-with-profile.html', {'albums': albums})


def album_add(request):
    form = CreateAlbumForm(request.POST or None)
    if form.is_valid():
        album = form.save(commit=False)
        album.profile = Profile.objects.first()
        album.save()
        return redirect('home-page')

    return render(request, 'add-album.html', {'form': form})


def album_details(request, id):
    album = Album.objects.get(id=id)
    return render(request, 'album-details.html', {'album': album})


def album_edit(request, id):
    album = Album.objects.get(id=id)
    form = EditAlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('home-page')

    return render(request, 'edit-album.html', {'form': form, 'album': album})


def album_delete(request, id):
    album = Album.objects.get(id=id)
    form = DeleteAlbumForm(request.POST or None, instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home-page')

    for field in form.fields.values():
        field.widget.attrs['disabled'] = True

    return render(request, 'delete-album.html', {'form': form, 'album': album})

def profile_details(request):
    profile = Profile.objects.first()
    albums_count = Album.objects.all().count()
    return render(request, 'profile-details.html', {'profile': profile, 'albums_count': albums_count})

def profile_delete(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        profiles.delete()
        return redirect('home-page')

    return render(request, "profile-delete.html")