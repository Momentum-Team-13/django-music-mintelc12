"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from junietunes import views as junietunes_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", junietunes_views.list_albums, name="list_albums"),
    path("junietunes/new/", junietunes_views.add_album, name="add_album"),
    path("junietunes/<int:pk>", junietunes_views.album_detail, name="album_detail"),
    path("junietunes/<int:pk>/edit", junietunes_views.edit_album, name="edit_album"),
    path("junietunes/<int:pk>/delete", junietunes_views.delete_album, name="delete_album"),
    path('contacts/<int:pk>/notes/', junietunes_views.add_note, name='view_note'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)