from django.views.generic import  View
from django.shortcuts import redirect, get_object_or_404
from gallery.models import Photo
from django.http import JsonResponse, HttpResponse
import json



def test(request):
    if request.method == "GET":
        answer = {
            "answer": "result"
        }
        HttpResponse.status_code = 200
        if request.body:
            answer['content'] = json.loads(request.body)
        return JsonResponse(answer)    

class FavoriteView(View):
    def get(self, request, *args, **kwargs):
        account = self.request.user
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        if account.favorites.filter(pk=kwargs['pk']):
            account.favorites.remove(photo)
            answer = {
                "answer": "result"
            }
            HttpResponse.status_code = 200
            if request.body:
                answer['content'] = json.loads(request.body)
            return JsonResponse(answer)    
        else:
            account.favorites.add(photo)
            answer = {
                "answer": "result"
            }
            HttpResponse.status_code = 200
            if request.body:
                answer['content'] = json.loads(request.body)
            return JsonResponse(answer)    



