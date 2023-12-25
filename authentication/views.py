from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm

# Create your views here.

class SignUp(generic.CreateView):
    form_class = SignupForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_invalid(self):
        messages.warning(self.request, "Please enter details properly")
        return redirect("register")  # Redirect to the register page on form invalid
    
class LoginUser(generic.View):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("home")
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(
                        request, f"You are logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "Username or password incorrect")
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
class LogoutUser(generic.View):
    
    def get(self, request):
        logout(request)
        return redirect('login')
        