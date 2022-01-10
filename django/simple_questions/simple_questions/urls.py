from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.routers', 'accounts'), namespace='accounts')),
    path('api/', include(('api.routers', 'api'), namespace='api'))
]
