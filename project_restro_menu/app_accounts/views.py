from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.views import View
from django.contrib import auth

# Create your views here.
# login ra register lai hamle authenticate garna rakeko ho
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')


class LoginView(View):
    def get(self,request):
        return render(request,'accounts/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist as error:
            print(error)

        if user is not None:
            login(request, user)
            return redirect('menu-list')
        return redirect('login')

class RegisterView(View):
    def get(self,request):
        return render(request,'accounts/register.html')

    def post(self,request):
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username,email = email, password =password) 
        
        if user is not None: 
            user.first_name = fname
            user.last_name = lname
            user.is_active =True
            user.save()
            return redirect ('login')
        return redirect ('register')