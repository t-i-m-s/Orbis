from django.urls import path
from . import views


urlpatterns = [
    path('object/<str:id>/', views.set_json),
    path('object/', views.set_json),
]
