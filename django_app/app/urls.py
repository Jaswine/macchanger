from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.core.signing import Signer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]

handler404 = "app.views.page_not_found_view"
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)