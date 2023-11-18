from base64 import urlsafe_b64decode
from cgitb import handler
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('virus_total/<str:ip_address>/', views.virus_total_view, name='virus_total'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
