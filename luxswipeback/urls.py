from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    # path('api/posts/', include('posts.urls')),
    # path('api/wardrobes/', include('wardrobes.urls')),
    # path('api/external-stores/', include('external_stores.urls')),
]