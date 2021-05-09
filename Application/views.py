from django.shortcuts import render
from Application.models import Application

# Create your views here.
def home_view(request):
    object_list = Application.objects.all()
    return render(request, '/home/wolf/WebRender/template/index.html',{
        'object_list': object_list,
        'nav':'index'
    })
def about_view(request):
    return render(request, '/home/wolf/WebRender/template/about.html' ,{
        'nav':'about'
    })