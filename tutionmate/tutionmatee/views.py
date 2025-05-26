
from .models import teacher,subjects
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateTeacherForm


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
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'signup.html')


def create_teacher_view(request):
    if request.method == 'POST':
        form = CreateTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher_obj = form.save(commit=False)
            # Here, if you want to hash password, do it before saving:
            # teacher_obj.password = hash_password_function(form.cleaned_data['password'])
            teacher_obj.save()
            form.save_m2m()  # For ManyToManyField, save after saving object
            return redirect('tutionmate:homepage')  # Redirect after successful form submit
    else:
        form = CreateTeacherForm()

    return render(request, 'create_teacher.html', {'form': form})
# Create your views here.
