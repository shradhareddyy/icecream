from django.contrib import admin
from .router import router
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libraryapi/', include(router.urls)),
]
