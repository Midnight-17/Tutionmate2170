from django.shortcuts import render
from .models import teacher,subjects
from django.http import JsonResponse

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


def data(request):
    teachers = teacher.objects.all()
    
    data = []
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

# Create your views here.
