from django.shortcuts import render, redirect
 
from app.models import servise
from app.forms import search

servises = servise.objects.all()
all_city = ['bhopal','bilaspur','bhilai','pendra']
all_servises = ['plumber','electrician','carpenter','painter','mechanic','sanitization']
all_state = ['cg','mp']
# Create your views here.
def index(request):
    
    all_city = ['bhopal','bilaspur','bhilai','pendra']
    all_servises = ['plumber','electrician','carpenter','painter','mechanic','sanitization']
    all_state = ['cg','mp']
    return render(request, 'index.html',{'all_city':all_city, 'all_servises':all_servises, 'all_state':all_state, 'servises':servises})

def list(request):
    if request.method == "POST":
        search_form = search(request.POST)
        if search_form.is_valid():
            servise_type = search_form.cleaned_data['servise_type']
            city = search_form.cleaned_data['city']
            state = search_form.cleaned_data['state']
            search_servises = servise.objects.filter(servise_type=servise_type, city=city, state=state).all()
            return render(request, 'list.html', {'servises':search_servises,'all_city':all_city, 'all_servises':all_servises, 'all_state':all_state})    
    return redirect('index')    

def profile(request,id):
    servise_profile = servise.objects.filter(id=id).first()
    return render(request, 'profile.html',{'all_city':all_city, 'all_servises':all_servises, 'all_state':all_state})    


def add_service(request):

    return render(request, 'add_service.html',{'all_city':all_city, 'all_servises':all_servises, 'all_state':all_state,'profile':servise_profile})    