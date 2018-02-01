from django.urls import path, include

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
