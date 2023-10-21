from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('get_test/', views.get_test),
    path('page1/<int:num>/', views.page1),
    path('page2/', views.page2)
]