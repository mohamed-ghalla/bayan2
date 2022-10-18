#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

#urlpatterns = [
#    path("bayanApp/", include("bayanApp.urls")),
#    path("", include("bayanApp.urls")),
#]
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


#admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=  i18n_patterns(
    path('', include('bayanApp.urls')),
    prefix_default_language=False,) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 


#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT),
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

