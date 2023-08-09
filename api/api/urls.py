from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("gym_monitor.urls")),
    path('user/', include("user.urls")),
    path('store/', include("gym_store.urls"))
]

urlpatterns += [
    path('api-auth', include('rest_framework.urls')),
]
