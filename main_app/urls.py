from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name='home')
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('rooms/', views.RoomList.as_view(), name = 'rooms_index')
]