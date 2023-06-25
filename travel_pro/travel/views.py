from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Profile

# Create your views here.
def index(request):
    obj = Place.objects.all()
    obj_1 = Profile.objects.all()
    return render(request, 'index.html', {'result': obj, 'people': obj_1})
