import os

from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect

from accounts.models import Profile
from .models import Makeup

def makeup_list(request):
    makeups = Makeup.objects.all()
    return render(request, 'makeups/index.html', {'makeups': makeups})

def makeup_detail(request, pk):
    makeup = Makeup.objects.get(pk=pk)
    products = makeup.products.all()
    return render(request, 'makeups/makeup_detail.html', {'object': makeup, 'products': products})

def virtual_makeup(request, pk):
    makeup = Makeup.objects.get(pk=pk)

    makeup_image = str(makeup.image)
    user_image = str(request.user.profile.image)

    root = 'CPM/imgs/'

    save_path = root + 'results/'

    cmd = f'CUDA_VISIBLE_DEVICES=0 python CPM/main.py --style {root}{makeup_image} --input {root}{user_image}  --savedir {save_path} --filename {pk}_{request.user.id}.png'

    os.system(cmd)

    result = f'/{save_path}{pk}_{request.user.id}.png'

    return render(request, 'makeups/result.html', {'makeup': makeup, 'result': result})




