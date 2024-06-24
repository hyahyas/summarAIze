from django.contrib import admin
from django.urls import path
from prj1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('', views.homePage, name='homePage'),
    path('summarize/', views.summarize, name='summarize'),
    path('semantic/', views.semanticAnalysis, name='semanticAnalysis'),
    path('text-to-audio/', views.textToAudio, name='textToAudio'),
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
