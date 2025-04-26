from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import todo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == "POST":
        task = request.POST.get('task')
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()

    all_todos = todo.objects.filter(user=request.user)
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        valid = authenticate(username=username, password=password)

        if valid is not None:
            login(request, valid)
            return redirect('home-page')
        else:
            messages.error(request, 'User not found')
            return redirect('login-page')
            
    return render(request, 'todoapp/login.html', {})


def register(request):

    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        if len(password) < 5:
            messages.error(request,'pass is too short')
            return redirect('register-page')
        
        all_users=User.objects.filter(username=username)
        if all_users:
            messages.error(request,'choose another name')
            return redirect('register-page')


        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()


    return render(request,'todoapp/login.html',{})

@login_required
def DeleteTask(request,name):
    get_todo=todo.objects.get(user=request.user,todo_name=name)
    get_todo.delete()
    return redirect('home-page')

@login_required
def Update(request,name):
    get_todo=todo.objects.get(user=request.user,todo_name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('home-page')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('login-page')


