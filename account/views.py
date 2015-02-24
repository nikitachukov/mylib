from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf

# Create your views here.

# def login(request):
# return render(request, "auth/login.html")
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render_to_response('account/login.html', args)
    else:
        return render_to_response('account/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

def createuser(request):
    try:
        u = User.objects.create_superuser(username='nikitos', email='xx@xx.ru', password="admin4all")
        u.save()
        return render_to_response("account/result_message.html")
    except Exception as E:
        return render_to_response("account/result_message.html", {'error_message': {'error_message': str(E)}})