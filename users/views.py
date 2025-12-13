from django.shortcuts import render
from django.views import View
from .forms import Login,Profile,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import CustomUser



class UserLoginView(View):
    def get(self, request):
        form = Login()  # ❗️ signup form emas
        return render(request, "pages/login.html", {"form": form})

    def post(self, request):
        form = Login(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Login yoki parol noto‘g‘ri!")
        
        return render(request, "pages/login.html", {"form": form})


def profile_view(request):
    

    if request.method == 'PUT':
        profile = Profile(request.FORM)
        if profile.is_valid():
            profile
    else:
        form = Profile(instance=request.user)
        return render(request,'pages/profile.html',{"form":form})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')



class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        context={
            "form":form
        }
        return render(request,'pages/register.html',context=context)
    

    def post(self,request):
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users:login')
        else:
            form = RegisterForm()

        return render(request, 'pages/register.html', {'form': form})

