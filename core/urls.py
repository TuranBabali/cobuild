from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from home.views import test1, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/',test1 ,name='test1'),
    path('index/',index ,name='index'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
