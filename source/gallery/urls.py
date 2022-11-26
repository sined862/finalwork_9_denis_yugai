from django.urls import path
from gallery.views import PhotoCreationView, IndexView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView, FavoriteView, FavoriteListView
from accounts.views import logout_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo_add/', PhotoCreationView.as_view(), name='photo_add'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo'),
    path('photo/update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/del/<int:pk>', PhotoDeleteView.as_view(), name='photo_del'),
    path('photo/favorite/<int:pk>', FavoriteView.as_view(), name='favorite'),
    path('favorite/', FavoriteListView.as_view(), name='favorites'),
    path('logout/', logout_view, name='logout'),
]