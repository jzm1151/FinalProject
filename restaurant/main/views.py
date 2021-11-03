from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def home(request):
	return render(request, 'main/home.html')

def menu(request):
	menu = MenuItem.objects.all()
	context = {'menu' : menu}
	return render(request, 'main/menu.html', context)
