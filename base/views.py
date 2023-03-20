from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login_view_r(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginr.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'loginr.html')
    
def login_view_s(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            return redirect('home')
        else:
            return render(request, 'logins.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'logins.html')
    

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def success_s(request):
    return render(request,'jobs_available.html')

def success_r(request):
    return render(request,'success_r.html')

def jobs_creation(request):
    # if request.method == 'POST':
    #     uh
    return render(request,'jobs_creation.html')

def jobs_recruit_view(request):
    return render(request,'total_jobs_posted.html')
