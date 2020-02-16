from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.


def login(request ):
    return render(request,'login.html')

   

    

            

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(first_name=first_name,username=username,password=password1,last_name=last_name,email=email)
        user.save()
        return redirect('/')
    else:
    
        return render(request,'register.html')
