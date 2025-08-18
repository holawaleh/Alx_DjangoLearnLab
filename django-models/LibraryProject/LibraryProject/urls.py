# LibraryProject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # ✅ Include all bookshelf URLs
]