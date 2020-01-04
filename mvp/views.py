from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm

# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST["your_name"]
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'mvp/thanks.html', {'name': name})

    else:
        form = NameForm()


    return render(request,'mvp/index.html', {'form': form})
