from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Operation
from apps.accounts.models import User


def indexPage(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Usuário não autenticado. Faça o login.')
        return redirect('login_page')

    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Usuário não existe.')
        return redirect('login_page')
    
    panel = ''

    operations_history = Operation.objects.filter(user_id=user)

    if request.method == 'POST':
        parameters = request.POST.get('parameters')
        result = request.POST.get('result')

        Operation.objects.create(
            parameters=parameters,
            result=result,
            user_id=user
        )
        panel = result

        return render(request, 'page/index.html', {'result': panel, 'operations_history': operations_history})
    

    return render(request, 'page/index.html', {'result': panel, 'operations_history': operations_history})


def logout(request):
    request.session.pop('user_id', None)
    return redirect('login_page')

def clearHistory(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Usuário não autenticado. Faça o login.')
        return redirect('login_page')

    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Usuário não existe.')
        return redirect('login_page')
    
    operations_history = Operation.objects.filter(user_id=user)

    for history in operations_history:
        history.delete()

    return redirect('index_page')

