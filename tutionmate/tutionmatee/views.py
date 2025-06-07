
from .models import teacher,subjects
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateTeacherForm, CreateUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

def admin(request):
    return render(request, "firstpage.html" , {
        "teachers": teacher.objects.all(),
    })

def test(request):
    return render(request, 'test.html')


def profile(request, tutor_name):
    return render(request, "profile.html", {
        "teacher" : teacher.objects.get(name = tutor_name)
    })


def data(request, start, end):
    teachers = teacher.objects.all()
    data = []
    x=start
    for t in teachers:
        data.append({
            'name': t.name,
            'rate_min': t.rate_min,
            'rate_max': t.rate_max,
            'subjects': [s.type for s in t.subjects.all()],
        })
    

    return JsonResponse({'teachers': data})




def discover(request):
    return render(request, "discover.html",{
        "teachers":teacher.objects.all()
    })

def homepage(request):
    return render(request, 'homepage.html',
            {"teachers":teacher.objects.all()
                 })

def newdiscover(request):
    return render(request, 'newdiscover.html',{
        "teachers":teacher.objects.all()
    })


def loginpage(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "loginpage.html", {
        "form":form
    })


def signup(request):
    return render(request, 'signup.html')


def create_teacher_view(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "create_teacher.html", {
        "form":form
    })

def login1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tutionmate:homepage')

    return render(request, "login1.html")
# Create your views here
