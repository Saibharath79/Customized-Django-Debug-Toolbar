from django.contrib import admin
from django.urls import path
from debugapp.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('tictactoe/',TicTacToeView.as_view(),name="tictactoe")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)