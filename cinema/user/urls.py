from django.urls import path
from user import views
from user.views import UserProfileView


urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]