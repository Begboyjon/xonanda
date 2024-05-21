from django .urls import path
from .views import *

urlpatterns = [
    path('teacher/', teacher, name='teacher'),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('course/', course, name='course'),
    path('contact', contact, name='contact')
]
