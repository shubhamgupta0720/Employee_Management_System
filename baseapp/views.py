from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import EmployeeDataManager, Projects, ManagerData
from .forms import EmployeeDataManagerForm, ProjectsForm

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or password does not exists')

    context = {}
    return render(request, 'baseapp/loginpage.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'baseapp/home.html')

@login_required(login_url='login')
def employeedatadisplay(request):
    data = EmployeeDataManager.objects.all()
    context = {'data':data}
    return render(request, 'baseapp/employeedisplay.html', context)

@login_required(login_url='login')
def addNewEmployee(request):
    form = EmployeeDataManagerForm()
    if request.method == "POST":
        form = EmployeeDataManagerForm(request.POST)
        if form.is_valid():
            isManager = form.cleaned_data.get('isManager')
            if isManager:
                print(True)
            form.save()
            return redirect('employeedisplay')
    context = {'form':form}
    return render(request, 'baseapp/addeditEmployee.html', context)

@login_required(login_url='login')
def editEmployee(request, pk):
    data = EmployeeDataManager.objects.get(employee_id=pk)
    form = EmployeeDataManagerForm(instance=data)

    if request.method == "POST":
        form = EmployeeDataManagerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('employeedisplay')

    context = {'form':form}
    return render(request, 'baseapp/addeditEmployee.html', context)

@login_required(login_url='login')
def deleteEmployee(request, pk):
    data = EmployeeDataManager.objects.get(employee_id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('employeedisplay')

    context = {'id':data.employee_name}
    return render(request, 'baseapp/deleteEmployee.html', context)

@login_required(login_url='login')
def projectsDisplay(request):
    projects = Projects.objects.all()
    context = {'projects':projects}
    return render(request, 'baseapp/projectdisplay.html', context)

@login_required(login_url='login')
def addNewProject(request):
    form = ProjectsForm()
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projectdisplay')
    context = {'form':form}
    return render(request, 'baseapp/addeditProject.html', context)

@login_required(login_url='login')
def editProject(request, pk):
    data = Projects.objects.get(project_id=pk)
    form = ProjectsForm(instance=data)

    if request.method == "POST":
        form = ProjectsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('projectdisplay')

    context = {'form':form}
    return render(request, 'baseapp/addeditProject.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    data = Projects.objects.get(project_id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('projectdisplay')

    context = {'id':data.project_name}
    return render(request, 'baseapp/deleteEmployee.html', context)