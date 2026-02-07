from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views_admin

urlpatterns = [
    path('', views.home, name='home'),
    path('resort/<int:resort_id>/', views.resort_detail, name='resort_detail'),
    path('resort/<int:resort_id>/room/<int:room_type_id>/', views.room_detail, name='room_detail'),
    path('resort/<int:resort_id>/room/<int:room_type_id>/book/', views.book_room, name='book_room'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Admin URLs
    path('custom-admin/', views_admin.admin_dashboard, name='admin_dashboard'),
    path('custom-admin/resorts/', views_admin.admin_resort_list, name='admin_resort_list'),
    path('custom-admin/resorts/add/', views_admin.admin_resort_create, name='admin_resort_create'),
    path('custom-admin/resorts/<int:pk>/edit/', views_admin.admin_resort_update, name='admin_resort_update'),
    path('custom-admin/resorts/<int:pk>/delete/', views_admin.admin_resort_delete, name='admin_resort_delete'),

    path('custom-admin/rooms/', views_admin.admin_room_list, name='admin_room_list'),
    path('custom-admin/rooms/add/', views_admin.admin_room_create, name='admin_room_create'),
    path('custom-admin/rooms/<int:pk>/edit/', views_admin.admin_room_update, name='admin_room_update'),
    path('custom-admin/rooms/<int:pk>/delete/', views_admin.admin_room_delete, name='admin_room_delete'),



    path('custom-admin/reservations/', views_admin.admin_reservation_list, name='admin_reservation_list'),
    path('custom-admin/reservations/<int:pk>/update/', views_admin.admin_reservation_update, name='admin_reservation_update'),
    path('custom-admin/users/', views_admin.admin_user_list, name='admin_user_list'),
]
