from django.urls import path, register_converter
from . import views, converters
from django.conf import settings
from django.conf.urls.static import static

register_converter(converters.IdListConverter, 'id_list')

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('login', views.my_login, name='login'),
    path('cart', views.cart, name='cart'),
    path('testing/<id_list:id_list>', views.testing, name='testing'),
    path('validate_username', views.validate_username, name='validate_username'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
