from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.statics import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('movies.urls'))
    path('api/', include('recommender.urls'))
    path('api/', include('profiles.urls'))
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
