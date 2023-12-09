from django.urls import path
from . import views

urlpatterns = [
    path('participations/', views.Participations.as_view()),
    path('paper/competition/<int:cid>/', views.PaperCompetition.as_view()),
    path('paper/participations/<int:pid>/score/', views.Score.as_view()),
]