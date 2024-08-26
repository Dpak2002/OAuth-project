from django.urls import path
from .views import (
    CreateUserAPI,
    ListUserAPI, 
    DetailUserAPI
)
urlpatterns = [
    path('create/', CreateUserAPI.as_view(), name='create_user'),
    path('list/', ListUserAPI.as_view(), name='create_user'),
    path('user/<pk>', DetailUserAPI.as_view(), name='user_details'),

]