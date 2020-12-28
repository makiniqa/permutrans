from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item 
from .forms import ItemForm

# Create your views here.

@login_required(login_url='login')
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemForm()
    context = {
        'form': form
    }
    return render(request, "item-create.html", context)

@login_required(login_url='login')
def item_all(request):
    queryset = Item.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "placard.html", context)

@login_required(login_url='login')
def item_select(request):
    user = request.user
    queryset = Item.objects.filter(user=user)
    context = {
        'object' : queryset
    }
    return render(request, "placard.html", context)