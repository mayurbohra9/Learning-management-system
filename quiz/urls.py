from django.urls import path
from . import views

app_name='quiz'
urlpatterns = [
    path("quizhome",views.quizhome, name ="quizhome"),
    path("api/get-quiz/", views.get_quiz,name='get_quiz'),
    path("quiz/", views.quiz,name='quiz'),    
]
