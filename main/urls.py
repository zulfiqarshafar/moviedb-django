from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
