from django.urls import path

from MyMusicApp.music.views import album_add, home_page, album_details, profile_details, profile_delete, album_edit, \
    album_delete

urlpatterns =[
    path('',  home_page, name='home-page'),
    path('album/add/', album_add, name='add-album'),
    path('album/details/<int:id>/', album_details, name='album-details'),
    path('album/edit/<int:id>/', album_edit, name='album-edit'),
    path('album/delete/<int:id>/', album_delete, name='album-delete'),
    path('profile/',profile_details, name='profile-details'),
    path('delete/',profile_delete, name='profile-delete'),

]