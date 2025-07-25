from django.shortcuts import render


def loginPage(request):


    return render(request, 'page/login.html')


def registerPage(request):


    return render(request, 'page/register.html')
