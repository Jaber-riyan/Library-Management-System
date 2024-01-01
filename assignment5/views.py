from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from books.models import BookModel, UserModel
from categories.models import CategoryModel



def home(request,book_category_slug=None):
    book = BookModel.objects.all()
    
    if book_category_slug is not None:
        category = CategoryModel.objects.get(slug=book_category_slug)
        book = BookModel.objects.filter(category=category)
        
    category = CategoryModel.objects.all()
        
        
    return render(request,'home.html',{'book':book,'category':category})



def signupview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Create Successfully')
                form.save()
                return redirect('homepage')
        else:
            form = forms.SignUpForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('homepage')
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        messages.success(self.request,'Login Successfully')
        return reverse_lazy('homepage')


def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = username, password = userpass)
            if user is not None:
                messages.success(request,'Login Successfully')
                login(request,user)
                return redirect('homepage')
            else:
                messages.success(request,'Login information incorrect')
                return redirect('signuppage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(request=self.request)
            
        messages.info(self.request,'Logout Successfully')
        return reverse_lazy('homepage')
    

@login_required   
def deposite(request):
    if request.method == 'POST':
        user = UserModel.objects.get(user=request.user)
        form = forms.depositeForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user.balance += amount
            user.save()
            messages.success(request,'Deposite Successfully Added')
            return redirect('homepage')
            
    else:
        form = forms.depositeForm()
    return render(request,'deposite.html',{'form':form})
    