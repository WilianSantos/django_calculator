from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import User


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'E-mail não cadastrado.')
            return render(request, 'page/login.html')

        if user.check_password(password): 
            request.session['user_id'] = user.user_id
            return redirect('index_page')
        else:
            messages.error(request, 'Senha incorreta.')
            return render(request, 'page/login.html')

    return render(request, 'page/login.html')


def registerPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'E-mail inválido.')
            return render(request, 'page/register.html')

        if password != confirm_password:
            messages.error(request, 'Senhas diferentes.')
            return render(request, 'page/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'page/register.html')
        
        if not all([name, email, password, confirm_password]):
            messages.error(request, 'Preencha todos os campos.')
            return render(request, 'page/register.html')

        user = User(name=name, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login_page')

    return render(request, 'page/register.html')

