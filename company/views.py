from django.shortcuts import render
from .models import *


def teacher(request):
    teachers = Teachers.objects.all().order_by('-id')
    context = {
        'teachers': teachers
    }
    return render(
        request=request,
        template_name='teacher.html',
        context=context
    )

def home(request):
    return render(request, 'index.html')

def about(request):
    abouts = Abouts.objects.all().order_by('-id')
    context = {
       'abouts': abouts
    }
    return render(
        request=request,
        template_name='about.html',
        context=context
    )

def course(request):
    return render(request, 'course.html')



def contact(request):
    contacts = Contacts.objects.all().order_by('-id')
    context = {
        'contacts': contacts
    }
    return render(request, 'contact.html', context)
