from django.urls import path
from wallet1 import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('status', views.status)
]
