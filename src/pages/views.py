from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
 
def home_page(request):
    print(request.user)
    context = {}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def profile_page(request):
    context = {
        'user' : request.user
    }
    return render(request, 'profile.html', context)