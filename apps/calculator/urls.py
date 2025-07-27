from django.urls import path

from .views import indexPage, logout, clearHistory


urlpatterns = [
    path('home', indexPage, name='index_page'),
    path('logout', logout, name='logout'),
    path('clear-history', clearHistory, name='clear_history'),
]
