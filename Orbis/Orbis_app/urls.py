from django.urls import path
from . import views


urlpatterns = [
    path('object/<int:id>/', views.set_json),
    path('object/', views.set_json),
]
