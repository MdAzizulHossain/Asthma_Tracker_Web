from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from AsthmaTracker.admin import Doctor


# Create your views here.


def index(request):
    context = {}
    return render(request, 'AsthmaTracker/index.html', context)


def admin_home(request):
    context = {}
    return render(request, 'AsthmaTracker/admin_home.html', context)


def admin_login(request):
    context = {}
    return render(request, 'AsthmaTracker/admin_login.html', context)

def p_home(request):
    context = {}
    return render(request, 'AsthmaTracker/p_home.html', context)


def p_register(request):
    context = {}
    return render(request, 'AsthmaTracker/p_register.html', context)

def p_signin(request):
    context = {}
    return render(request, 'AsthmaTracker/p_signin.html', context)



def d_register(request):
    error = ""
    if not request.user.is_staff:
        return redirect('p_register')

    if request.method =='POST':
        a = request.POST['name']
        b = request.POST['phn']
        c = request.POST['email']
        # d = request.POST['reg_no']
        e = request.POST['spcl']
        f = request.POST['password1']
        try:
            Doctor.objects.create(name=a, mobile=b, email=c, specialization=e, password=f)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'AsthmaTracker/d_register.html', d)



def signin(request):
    # error=""
    #
    # if request.method == 'POST':
    #     u = request._post['uname']
    #     p = request._post['psw']
    #     user = auth(username=u,password=p)
    #     try:
    #         if user.is_staff:
    #             signin(request,user)
    #             error="no"
    #         else:
    #             error="yes"
    #     except:
    #         error="yes"
    # d = {'error':error}
    # return render(request,'AsthmaTracker/signin.html',d)

    context = {}
    return render(request, 'AsthmaTracker/signin.html', context)

def home(request):
    if not request.user.is_staff:
        return redirect('register')

    context = {}
    return render(request, 'AsthmaTracker/home.html', context)

def d_profile(request):
    context = {}
    return render(request, 'AsthmaTracker/d_profile.html', context)