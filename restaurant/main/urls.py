from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
	path('', views.home, name='home'),
	path('menu', views.menu, name='menu'),
	path('menu/sort/catagory', views.menu_catagory, name='menu_catagory'),	
	path('menu/sort/name', views.menu_name, name='menu_name'),
	path('menu/sort/price', views.menu_price, name='menu_price'),
	path('register', views.register, name='register'),
	path('logout', views.logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)