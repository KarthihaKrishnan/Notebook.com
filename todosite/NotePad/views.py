from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

## import Notepad form and models

from .forms import NotePadForm
from .models import NotePad


###############################################

def index(request):
    item_list = NotePad.objects.order_by("-date")
    if request.method == "POST":
        form = NotePadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('NotePad')
    form = NotePadForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "NOTEPAD LIST",
    }
    return render(request, 'NotePad/index.html', page)


### function to remove item, it receive NotePad item_id as primary key from url ###
def remove(request, item_id):
    item = NotePad.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('NotePad')
