from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'miradashop'

urlpatterns = [
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.view_favorites, name='view_favorites'),  # Новый маршрут
    path('products/', views.product_list, name='product_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
