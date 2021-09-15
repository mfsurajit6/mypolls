from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from user.forms import UserRegistrationForm


class RegistrationView(View):
    """Register a new user"""

    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'user/register.html', {'form':form, 'data': request.POST})

class CustomLoginView(LoginView):
    """Login User"""

    redirect_authenticated_user = 'index'
    def get(self, request):
        return render(request, 'user/login.html')
    
    def post(self, request, ):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'user/login.html',{'error':'Invalid Username or Password'})
    
    def get_success_url(self):
        return reverse_lazy('index')