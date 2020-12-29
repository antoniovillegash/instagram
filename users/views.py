"""users Views"""

#Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    """login view"""
    if request.method == 'POST':
        # print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        # print(username, ':',password)
        # print('*' * 10)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error':'Invalid username or password'})
    return render(request,'users/login.html')