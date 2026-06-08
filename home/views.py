from django.shortcuts import render
from django import http
from django.contrib.auth.decorators import login_required
from Oauth2.models import User
from django.http import JsonResponse

from json import loads
from .userData import UserData
def save_timezone(request):
    ''' Получение UTC пользователя'''
    if request.method == 'POST':
        request.session['user_timezone'] = loads(request.body).get('timezone')

        return JsonResponse({'message': 'Timezone saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def home(request, user = None):
    ''' Главная страница '''
    if request.method == "POST":
        if request.POST.get("delete_message") != None:
            UserData(request,user).delete_message()
            return http.HttpResponse(render(request, 'home.html', context=UserData(request,user).data()))

        if request.POST.get("delete_chat") != None:
            UserData(request,user).delete_chat()
            return http.HttpResponse(render(request, 'home.html', context=UserData(request,user).data()))

        if request.POST.get('edit_avatar') != None:
            return User.objects.get(username = request.user).edit_user(request)

        if request.POST.get('search') != None:
            return http.HttpResponseRedirect(f'/{User().search(request)}/')
        
        if request.POST.get('input_message') != None:
            UserData(request,user).send_message()
            return http.HttpResponse(render(request, 'home.html', context=UserData(request,user).data()))
            
    return render(request, 'home.html', context=UserData(request,user).data())

    