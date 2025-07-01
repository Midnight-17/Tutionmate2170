
from .models import teacher,subjects
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateTeacherForm, CreateUser,UserForm,TeacherForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth.decorators import login_required


def admin(request):
    return render(request, "firstpage.html" , {
        "teachers": teacher.objects.all(),
    })

@login_required
def test(request):
    user_instance = request.user
    teacher_instance = user_instance.teacher 
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user_instance)
        teacher_form = TeacherForm(request.POST, request.FILES, instance=teacher_instance)

        if user_form.is_valid() and teacher_form.is_valid():
            user_form.save()
            teacher_form.save()
            return redirect('tutionmate:homepage')  # change this to wherever you want to go next

    else:
        user_form = UserForm(instance=user_instance)
        teacher_form = TeacherForm(instance=teacher_instance)

    return render(request, 'test.html', {
        "user_form": user_form,
        "teacher_form": teacher_form
    })


def profile(request, tutor_name):
    return render(request, "profile.html", {
        "teacher" : teacher.objects.get(user__username = tutor_name)
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
    teachers_ = teacher.objects.all().order_by('?').distinct()
    first_four = teachers_[:4]
    second_four = teachers_[4:8]
    third_four = teachers_ [8:12]
    teachers = {
        "first_four":first_four ,
        "second_four" : second_four , 
        "third_four":third_four
    }


    if request.method == 'POST':
        search = request.POST.get('homepage-search-bar', '').strip()

        if search:
            matching_teachers = teacher.objects.filter(
                user__username__icontains=search
            )

            non_matching_teachers = teacher.objects.exclude(
                user__username__icontains=search
            ).order_by('?')

            teachers = list(matching_teachers) + list(non_matching_teachers)
        

            return render(request, 'newdiscover.html', {
                "teachers": teachers
            })

    else:
        return render(request, 'homepage.html',
                {"teachers": teachers
                    })

def newdiscover(request):
    return render(request, 'newdiscover.html',{
        "teachers":teacher.objects.all()
    })


def loginpage(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            # Save User
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Save Teacher
            teacher_obj = teacher.objects.create(
                user=user,
                image=form.cleaned_data['image'],
                min_rate=form.cleaned_data['min_rate'],
                max_rate=form.cleaned_data['max_rate'],
                phone_number = form.cleaned_data['phone_number']
            )
            teacher_obj.subjects.set(form.cleaned_data['subjects'])
            teacher_obj.save()

            # Redirect or login user
            return redirect('tutionmate:login1')  # or wherever you want

    else:
        form = CreateTeacherForm()
    
    return render(request, 'loginpage.html', {'form': form})


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
