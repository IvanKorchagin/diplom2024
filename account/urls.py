from django.urls import re_path, path
from django.contrib.auth.views import LogoutView, logout_then_login
from django.contrib.auth import views as auth_views
from . import views


app_name = "account"
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'), name='password_change'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
    