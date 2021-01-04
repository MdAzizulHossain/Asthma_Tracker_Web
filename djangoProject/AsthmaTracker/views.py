from django.shortcuts import render, redirect
from django.contrib.auth.forms import User


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



def register(request):
    if request.method == 'POST' :
        uname = request.POST['uname']
        # phone = request.POST['phone']
        email = request.POST['email']
        # spcl = request.POST['spcl']
        psw1 = request.POST['psw']
        # psw2-repeat = request.POST['psw2-repeat']

        user = User.objects.create_user(username=uname, password=psw1, email=email)
        user.save()
        print('User Created')
        return redirect('/')


    else:

        context = {}
        return render(request, 'AsthmaTracker/register.html', context)



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
