from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from miradashop.views import index
from orders.views import user_orders

urlpatterns = [
    path('', index, name='index'),
    path('orders/', include('orders.urls', namespace='orders')),
     path('my_orders/', user_orders, name='user_orders'),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('account/', include('account.urls', namespace='account')),
    path('handle_forms/', include('contact.urls', namespace='contact')),
    path('', include('miradashop.urls', namespace='miradashop')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)