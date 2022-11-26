from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse, reverse_lazy 
from django.shortcuts import redirect, get_object_or_404
from gallery.models import Photo, Favorites
from gallery.forms import PhotoForm
from django.contrib.auth.models import User





class PhotoCreationView(LoginRequiredMixin, CreateView):
    template_name = 'gallery/photo_add.html'
    form_class = PhotoForm
    model = Photo

    def post(self, *args, **kwargs):
        form_photo = PhotoForm(self.request.POST, self.request.FILES)
        author = get_object_or_404(User, pk=self.request.user.id)
        if form_photo.is_valid():
            photo = form_photo.save(commit=False)
            photo.author = author
            photo.save()
            return redirect('photo', pk=photo.pk)
        else:
            return render(self.request, 'gallery/photo_add.html', {'form': form_photo})

class PhotoDetailView(DetailView):
    template_name = 'gallery/photo.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id:
            account = get_object_or_404(User, pk=self.request.user.id)
            like_or_not = account.favorites.filter(pk=self.object.id)
            context['like_or_not'] = like_or_not
            if self.request.user.id == self.object.author.id:
                context['is_author'] = True
            else:
                context['is_author'] = False
        return context

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'gallery/photo_update.html'
    form_class = PhotoForm
    model = Photo

    def get_success_url(self):
        return reverse('photo', kwargs={'pk': self.object.pk})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('index')

class IndexView(ListView):
    template_name = 'gallery/index.html'
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.all().order_by('-created_at')

class FavoriteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        account = self.request.user
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        if account.favorites.filter(pk=kwargs['pk']):
            account.favorites.remove(photo)
            return redirect('photo', pk=kwargs['pk'])
        else:
            account.favorites.add(photo)
            return redirect('photo', pk=kwargs['pk'])


class FavoriteListView(LoginRequiredMixin, ListView):
    template_name = 'gallery/favorites.html'
    model = User
    context_object_name = 'photos'

    def get_queryset(self):
        account = get_object_or_404(User, pk=self.request.user.id)
        return account