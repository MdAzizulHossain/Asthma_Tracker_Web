from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'AsthmaTracker/register.html', context)
#
#
#
def signin(request):
    context = {}
    return render(request, 'AsthmaTracker/signin.html', context)

def home(request):
    context = {}
    return render(request, 'AsthmaTracker/home.html', context)
