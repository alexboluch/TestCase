from django.urls import path
from . import views

urlpatterns = [
    path('get-info/', views.get_info_gituser),
    path('view-info/', views.get_view),
]