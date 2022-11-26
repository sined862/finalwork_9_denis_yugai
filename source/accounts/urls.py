from django.urls import path
from accounts.views import RegisterUser, LoginUserView


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login')
]
