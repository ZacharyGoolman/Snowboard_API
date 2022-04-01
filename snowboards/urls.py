from django.urls import path
from . import views
import snowboards

urlpatterns = [
    path('', views.snowboards_list),
    path('<int:pk>/', views.snowboard_detail),
]
