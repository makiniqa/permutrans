from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
 
def home_page(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, 'profile.html', context)
    else:   
        return render(request, 'home.html', context)

@login_required(login_url='login')
def profile_page(request):
    context = {
        'user' : request.user
    }
    return render(request, 'profile.html', context)