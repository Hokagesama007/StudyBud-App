from django.contrib import admin
from django.urls import path, include
from .views import home,room,createRoom,updateRoom,deleteRoom,loginpage,logoutpage,register,deleteMessage,userProfile,updateUser,topicsPage,activityPage


urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('user-profile/<str:pk>/', userProfile, name='user-profile'),

    path('create-room/', createRoom, name='create-room'),
    path('update-room/<int:pk>/', updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>/', deleteMessage, name='delete-message'),

    path('login/', loginpage, name='login'),
    path('logout/', logoutpage, name='logout'),
    path('register/', register, name='register'),
    path('update-user/', updateUser, name='update-user'),
    path('topics/', topicsPage, name='topics'),
    path('activity/', activityPage, name='activity'),


]