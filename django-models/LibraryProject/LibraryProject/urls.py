# LibraryProject/urls.py
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from relationship_app import views as relationship_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Bookshelf at root
    path('', include('bookshelf.urls')),

    # Relationship app under /relationship/
    path('relationship/', include('relationship_app.urls')),
]