from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Makeup

app_name = 'makeups'

urlpatterns = [
    path('', makeup_list, name='makeup_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Makeup, template_name='makeups/makeup_detail.html'), name='makeup_detail'),
    path('detail/<int:pk>/makeup/',virtual_makeup, name='virtual_makeup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)