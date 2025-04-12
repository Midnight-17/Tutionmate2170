from django.shortcuts import render
from .models import teacher,subjects

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


# Create your views here.
