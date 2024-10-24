from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_contact_info/', views.update_contact_info, name='update_contact_info'),
    path('add_reference/', views.add_reference, name='add_reference'),
    path('add_experience/', views.add_experience, name='add_experience'),
    path('delete_reference/<int:id>', views.delete_reference, name='delete_reference'),
    path('delete_experience/<int:id>', views.delete_experience, name='delete_experience'),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
]
