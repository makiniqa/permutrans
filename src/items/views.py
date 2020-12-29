from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item 
from .forms import ItemForm, DeleteForm
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        prenda = form.save(commit=False)
        prenda.user = User.objects.get(username=request.user)
        prenda.save()
        return redirect('all')
    context = {
        'form': form
    }
    return render(request, "item-create.html", context)

@login_required(login_url='login')
def item_all(request):
    queryset = Item.objects.filter(user=request.user)
    context = {
        'object_list' : queryset
    }
    return render(request, "placard.html", context)

@login_required(login_url='login')
def item_detail(request, pk):
    obj = Item.objects.get(id=pk)
    context = {
       'object' : obj 
    }
    return render(request, "item-detail.html", context)

@login_required(login_url='login')
def item_update(request, item_id):
    item_id = int(item_id)
    try:
        selected = Item.objects.get(id = item_id)
    except Item.DoesNotExist:
        return redirect('all')
    form = ItemForm(request.POST or None, instance = selected)
    if form.is_valid():
        prenda = form.save(commit=False)
        prenda.user = User.objects.get(username=request.user)
        prenda.save()
        return redirect('all')
    return render(request, 'item-update-form.html', {'form':form})

@login_required(login_url='login')
def item_delete(request, item_id):
    item_id = int(item_id)
    try:
        selected = Item.objects.get(id = item_id)
    except Item.DoesNotExist:
        return redirect('all')
    selected.delete()
    return render(request, 'item-delete.html', {})