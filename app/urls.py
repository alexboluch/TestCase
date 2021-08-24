from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('get-info/', views.get_info_gituser),
    path('view-info/', views.get_view),
    path('', views.get_info_gituser),
]