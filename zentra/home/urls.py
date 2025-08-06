from django.urls import path
from home.views import anasayfa
from home.views import giris
from home.views import hakkimizda
from home.views import baslat
from home.views import bilgisayar
from home.views import elektrik
from home.views import makine
from home.views import endustri 
from . import views
from .views import gemini_chat



urlpatterns = [
    path("", anasayfa, name="anasayfa"),
    path("giris/", giris, name="giris"),
    path("hakkimizda/", hakkimizda, name="hakkimizda"),
    path("baslat/", baslat, name="baslat"), 
    path('bilgisayar/', bilgisayar, name='bilgisayar'),
    path('elektrik/', elektrik, name='elektrik'),
    path('makine/', makine, name='makine'), 
    path('endustri/', endustri, name='endustri'), 
    path('api/gemini-chat/', gemini_chat, name='gemini_chat'),  
    path('learning-path/', views.gemini_learning_path, name='gemini_learning_path'),
    path('code-analysis/', views.gemini_code_analysis, name='gemini_code_analysis'),
]
