from django.urls import path
from . import views
import snowboards

urlpatterns = [
    path('', views.snowboards_list),
]
