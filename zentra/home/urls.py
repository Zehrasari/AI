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
path('gemini-chat/', views.gemini_chat, name='gemini_chat'),
path("", anasayfa),#tırnak içindeki boşluk anasayfa.html dosyasını bulur
path("giris/", giris),
path("hakkimizda/", hakkimizda),
path("baslat/", baslat), 
path('bilgisayar/', views.bilgisayar, name='bilgisayar'),
path('elektrik/', views.elektrik, name='elektrik'),
path('makine/', views.makine, name='makine'), 
path('endustri/', views.endustri, name='endustri'), 
path('gemini-chat/', gemini_chat, name='gemini-chat'),

]
