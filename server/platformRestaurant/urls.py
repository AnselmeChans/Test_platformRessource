
from knox import views as knox_views


from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserAPI, RoomSerialiser, RoomAPI



urlpatterns = [
  path('api/auth', include('knox.urls')),
  path('api/auth/register', RegisterAPI.as_view()),
  path('api/auth/login', LoginAPI.as_view()),
  path('api/auth/user', UserAPI.as_view()),
  path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'), 
  path('api/auth/restaurant', RoomAPI.as_view()),
]




