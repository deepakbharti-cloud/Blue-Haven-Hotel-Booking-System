from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='hotel_list'),path('<int:pk>/',views.hotel_detail,name='hotel_detail'),path('room/<int:pk>/',views.room_detail,name='room_detail'),path('owner/add/',views.owner_hotel_create,name='hotel_create'),path('owner/<int:hotel_id>/rooms/add/',views.room_create,name='room_create'),path('<int:hotel_id>/review/',views.review_create,name='review_create')]
