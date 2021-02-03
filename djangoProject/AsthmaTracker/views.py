from django.shortcuts import render, redirect
from pyrebase import pyrebase
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from AsthmaTracker.admin import Doctor

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
    error = ""
    if not request.user.is_staff:
        return redirect('p_register')

    if request.method == 'POST':
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
    d = {'error': error}
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
