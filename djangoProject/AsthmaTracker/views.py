from django.shortcuts import render, redirect , HttpResponse
from pyrebase import pyrebase
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from requests import request
from django.contrib.auth.models import User
from AsthmaTracker.admin import Doctor
from django.http import HttpResponse



firebaseConfig = {
    'apiKey': "AIzaSyCCiIcPA41_rZ3KO31OXHfq8BKVmD20FP4",
    'authDomain': "asthma-tracker-fa7ac.firebaseapp.com",
    'databaseURL': "https://asthma-tracker-fa7ac.firebaseio.com",
    'projectId': "asthma-tracker-fa7ac",
    'storageBucket': "asthma-tracker-fa7ac.appspot.com",
    'messagingSenderId': "836327073019",
    'appId': "1:836327073019:web:78fc987ed9417b0a9fbc5e",
    'measurementId': "G-XBNH0EN784"
}
firebase = pyrebase.initialize_app(firebaseConfig)

authe = firebase.auth()
database = firebase.database()


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


# Patient home page
def p_home(request):
    context = {}
    return render(request, 'AsthmaTracker/p_home.html', context)


# end

# Patient registration page
def p_register(request):
    context = {}
    return render(request, 'AsthmaTracker/p_register.html', context)


# end


# Patient signIn page
def p_signin(request):
    context = {}
    return render(request, "AsthmaTracker/p_signin.html", context)


# end


# Authenticated patient signIn method
def postsign(request):
    context = {}
    email = request.POST.get('email')
    psw = request.POST.get('psw')
    try:
        user = authe.sign_in_with_email_and_password(email, psw)
    except:
        message = "Invalid credentials!"
        return render(request, "AsthmaTracker/p_signin.html", {"message": message})
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "AsthmaTracker/p_home.html", context)


# end


# Patient logout method
def p_logout(request):
    auth.logout(request)
    return render(request, "AsthmaTracker/p_signin.html")


# end


# Patient account creation method
def postsignup(request):
    fullname = request.POST.get('uname')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    age = request.POST.get('age')
    weight = request.POST.get('wgt')
    passw = request.POST.get('psw')
    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "Unable to create account. Email already in use. Try again"
        return render(request, "AsthmaTracker/p_register.html", {"message": message})
    uid = user['localId']

    data = {"fullName": fullname, "phone": phone, "email": email, "age": age, "weight": weight, "password": passw}

    database.child("Patient").child(uid).set(data)

    return render(request, "AsthmaTracker/p_signin.html")


# end


# Patient profile page and method
def p_profile(request):
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info" + str(a))

    profile_info = database.child('Patient').child(a).get().val()

    info_list = []
    for i in profile_info:
        info_list.append(i)

    print(info_list)

    info = []
    for i in info_list:
        infos = database.child('Patient').child(a).child(i).get().val()
        info.append(infos)
    print(info)
    real_info = zip(info_list, info)
    return render(request, "AsthmaTracker/p_profile.html", {'real_info': real_info})


# end

def d_register(request):

    if request.method == 'POST':
        form = Doctor(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'],
                      regno=request.POST['regno'], spcl=request.POST['spcl'])

        form.save()
        print('Registered Successfully')
        context = {'form': form}
        return render(request, 'AsthmaTracker/d_profile.html',context)
    else:
        return render(request, 'AsthmaTracker/d_register.html' )


def signin(request):
    context = {}
    if request.method == 'POST':
        try:
            # Check User in DB
            email = request.POST['email']
            password = request.POST['password1']
            user_authenticate = auth.authenticate(email=email, password1=password)
            if user_authenticate != None:
                user = User.objects.get(email=email)
            try:
                data = Doctor.objects.get(email=user)
                auth.login(request, user_authenticate)
                print('Docter has been Logged')
                return redirect('AsthmaTracker/d_profile.html',context)

            except:
                return redirect('/')

            else:
                print('Login Failed')
                return render(request, 'AsthmaTracker/signin.html')
        except:
            return render(request, 'AsthmaTracker/signin.html')
    return render(request, 'AsthmaTracker/d_profile.html',context)

# Logout
def logout(request):
	auth.logout(request)
	print('Logout')
	return redirect('/')

def d_update(request):
    context = {}
    return render(request, 'AsthmaTracker/d_update.html', context)

def home(request):
    if not request.user.is_staff:
        return redirect('register')

    context = {}
    return render(request, 'AsthmaTracker/home.html', context)


def d_profile(request):
    print(request.user)
    userid = User.objects.get(email=request.user)
    if request.user:
        status = request.user
    if request.method == "POST":
        update = Doctor.objects.get(username=userid)
        update.name = request.POST['name']
        userdata = Doctor.objects.get(username=userid)

    context = {}
    return render(request, 'AsthmaTracker/d_profile.html', context)
