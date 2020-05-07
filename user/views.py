from django.shortcuts import render, redirect
from user.forms import LoginForms, AccountCreation
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.cache import cache

# Create your views here.

def log_in(request):
    if request.method == 'GET':
        if request.GET.get('next') is not None:
            request.session['next'] = request.GET.get('next', '/')
        else:
            request.session['next'] = None
    if request.method == 'POST':
        forms = LoginForms(request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            user = authenticate(request, username=cd['username'],
                                         password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.session['next'] != None:
                        next_url = request.session['next']
                        del request.session['next']
                        return HttpResponseRedirect(next_url)
                    else:
                        return redirect('home:dashboard')
                else:
                    messages.error(request, 'account inactive')
                    return redirect('user:login')
            else:
                messages.error(request, 'account does not exist')
                return redirect('user:login')
    else:
        forms = LoginForms()
        context = {
            'forms': forms
        }
        
    return render(request, 'user/login.html', context)

def account_creation(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Please logout before creating a new account')
        return redirect('home:dashboard')
    else:
        if request.method == 'POST':
            forms = AccountCreation(request.POST)
            if forms.is_valid():
                new_user = forms.save(commit=False)
                new_user.set_password(forms.cleaned_data['password2'])
                new_user.save()
                messages.success(request, 'user has been created')
                return redirect('user:login')
        else:
            forms = AccountCreation()
        context = {
            'forms': forms
        }
        return render(request, 'user/account_creation.html', context)
        


                


"""

Account Creation

"""