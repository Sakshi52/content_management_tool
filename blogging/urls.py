from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# urls handling admin route
	path('admin/', admin.site.urls),
	# urls handling blog routes
	path('', include('blogapp.urls')),
]
