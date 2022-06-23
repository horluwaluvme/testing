from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ClientCreateForm
from .models import *
# Create your views here.

def home(request):
    title = 'Welcome to XYZhotel'
    form = 'Identation is important'
    context = {
        "title": title,
        "test": form,
    }
    return render(request, "home.html",context)


def list_items(request):
    header = 'List of Items'
    queryset = Management_Post.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
    }
    return render(request, "list_items.html",context)

def add_items(request):
	form = ClientCreateForm(request.POST or None)
	if form.is_valid():
          form.save()
          return redirect('/list_items')
      
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)

