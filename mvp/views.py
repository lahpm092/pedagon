from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm

# Create your views here.
def index(request):

    if request.method == 'POST':
        object = request.POST["object"]
        question = request.POST["question"]
        answer = request.POST["answer"]
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'mvp/thanks.html', {'object': object, 'question': question, 'answer': answer})

    else:
        form = NameForm()


    return render(request,'mvp/index.html', {'form': form})
