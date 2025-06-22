from django.urls import path
from .views import get_users, create_user
urlpatterns = [
    path('users/', get_users, name='get-users'),
    path('users/create/', create_user, name='create-user')

]
