from django.shortcuts import render, redirect
from .models import MenuItem

from .forms import UserSignUpForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder


def home(request):
    return render(request, 'main/home.html')


def menu(request):
    menu_obj = MenuItem.objects.all()
    context = {'menu': menu_obj}
    return render(request, 'main/menu.html', context)


def sign_in(request):
    login_form = AuthenticationForm
    signup_form = UserSignUpForm
    context = {'login_form': login_form,
               'signup_form': signup_form
               }
    return render(request, 'main/sign_in.html', context)


def register(request):
    data = {
        'result': False
    }

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            user = authenticate(request, username=new_user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                data['result'] = True

    return JsonResponse(data)


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    return redirect('sign_in')


def logout_user(request):
    logout(request)
    return render(request, 'main/home.html')


def cart(request):
    return render(request, 'main/cart.html')


def testing(request, id_list):
    id_item = dict()
    for ident in id_list:
        id_item[ident] = json.dumps(
            list(MenuItem.objects.filter(id=ident).values('price', 'name', 'image', 'id'))[0], cls=DjangoJSONEncoder)

    return JsonResponse(id_item)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Username tried is taken'
    return JsonResponse(data)
