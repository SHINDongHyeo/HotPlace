from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('trip/', include('trip.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)