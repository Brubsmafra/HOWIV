from django.shortcuts import render, redirect
from blog.Forms import AssistForm
from blog.models import Assist

def home(request):
     data = {}
     data['db'] = Assist.objects.all()
     return render(request, 'Index.html', data)

def Formulario(request):
    data = {}
    data['Formulario'] = AssistForm()
    return render(request, 'Formulario.html', data)

def create(request):
    Formulario = AssistForm(request.POST or None)
    if Formulario.is_valid():
        Formulario.save()
        return redirect('home')

def view(request,pk):
        data = {}
        data['db'] = Assist.objects.get(pk=pk)
        return render(request, 'view.html', data)

def edit(request,pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    data['Formulario'] = AssistForm(instance=data['db'])
    return render(request, 'Formulario.html', data)

def update(request,pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    Formulario = AssistForm(request.POST or None, instance=data['db'])
    if Formulario.is_valid():
        Formulario.save()
        return redirect('home')

def delete(request, pk):
    db = Assist.objects.get(pk=pk)
    db.delete()
    return redirect('home')