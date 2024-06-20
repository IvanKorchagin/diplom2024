from django.urls import path
from .views import handle_forms
app_name="contact"

urlpatterns = [
    path('handle_forms/', handle_forms, name='handle_forms'),
]
