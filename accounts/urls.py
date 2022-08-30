from django.urls import path

from .views import *
from .models import Profile

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('profile/update', ProfileUpdateView.as_view(), name="profile-update")
]