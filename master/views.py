from django.shortcuts import redirect, render

from .models import *

# Create your views here.


def add_course(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        fee = request.POST['fee']
        crtb = course(
            course_name=cname,
            fee=fee
        )
        crtb.save()
        return redirect('/add_course')
    return render(request, 'course.html')


def student_fun(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        address = request.POST['address']
        age = request.POST['age']
        fkey = request.POST['cc']
        fil_fkey = course.objects.get(id=fkey)
        stdtb = student(
            course=fil_fkey,
            std_name=sname,
            std_address=address,
            std_age=age,
        )

        stdtb.save()

    courses = course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'student.html', context)


def show_std(request):
   
    x = student.objects.all()

    context = {'std_db': x
    
               }

    return render(request, 'show.html', context)
