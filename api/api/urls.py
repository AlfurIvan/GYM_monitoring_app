from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include("gym_monitor.urls")),
    path('user/', include("user.urls")),
    path('', include("gym_store.urls"))
]

urlpatterns += [
    path('api-auth', include('rest_framework.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

