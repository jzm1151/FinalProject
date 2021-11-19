from django.shortcuts import render
from .models import MenuItem

from django.contrib.auth.models import User
from .forms import UserSignUpForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'main/home.html')


def menu(request):
    menu_obj = MenuItem.objects.all()
    context = {'menu': menu_obj}
    return render(request, 'main/menu.html', context)


def menu_catagory(request):
    menu_obj = MenuItem.objects.order_by('catagory')
    context = {'menu': menu_obj}
    return render(request, 'main/menu.html', context)


def menu_name(request):
    menu_obj = MenuItem.objects.order_by('name')
    context = {'menu': menu_obj}
    return render(request, 'main/menu.html', context)


def menu_price(request):
    menu_obj = MenuItem.objects.order_by('price')
    context = {'menu': menu_obj}
    return render(request, 'main/menu.html', context)


def register(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            user = authenticate(request, username=new_user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)

            return render(request, 'main/home.html')

    form = UserSignUpForm()
    context = {'form': form}

    return render(request, 'main/register.html', context)


def logout_user(request):
    logout(request)
    return render(request, 'main/home.html')
