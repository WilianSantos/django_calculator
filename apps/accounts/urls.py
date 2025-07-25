from django.urls import path

from .views import loginPage, registerPage


urlpatterns = [
    path('', loginPage, name='login_page'),
    path('/register', registerPage, name='register_page'),
]
