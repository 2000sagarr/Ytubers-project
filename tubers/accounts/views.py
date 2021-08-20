from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
            

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_Password = request.POST['confirm_password']
        
        if password == conf_Password:
            if User.objects.filter(username=userName).exists():
                messages.error(request, "User Already Exist!")
                return redirect(request, 'register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email Already Exist!")
                    return redirect(request, 'register')
                else:
                    user = User.objects.create_user( first_name=firstName, last_name=lastName, username=userName, email=email, password=password)
                    user.save()
                    messages.success(request, "Account Created Successfully!")
                    return redirect('login')
        else:
            messages.error(request, "Password Do No Match!")
            return redirect('register')

    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

# decorators
@login_required(login_url="login")
def dashboard(request):
    return render(request, 'accounts/dashboard.html')