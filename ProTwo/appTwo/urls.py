from django.urls import path

from appTwo import views

urlpatterns = [
    path('', views.colorexperts),
    path('help/', views.help),
]
