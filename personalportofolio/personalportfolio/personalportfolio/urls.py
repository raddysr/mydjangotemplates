from os import stat
from django.contrib import admin
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home' ),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
