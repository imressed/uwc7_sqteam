from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import HttpResponse, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_GET)
from django.http import JsonResponse

from .forms import UserCreationForm

from django.contrib import messages



def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'index.html', {'login_form': login_form,
                                          'signup_form': signup_form})

@require_GET
def login_view(request):
    return render(request, 'index.html', {'show_login': True})

@require_GET
def signup_view(request):
    return render(request, 'index.html', {'show_signup': True})

@require_POST
def login_func(request):
    login_form = AuthenticationForm(data=request.POST)
    if login_form.is_valid():
        user = authenticate(username=login_form.cleaned_data.get('username'),
                            password=login_form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'next': '/app'})
    else:
        return JsonResponse({'success': False,
                             'errors': login_form.errors})

@require_GET
def logout_func(request):
    logout(request)
    return redirect('index')

@require_POST
def signup_func(request):
    signup_form = UserCreationForm(data=request.POST)
    if signup_form.is_valid():
        signup_form.save()
        messages.add_message(request, messages.INFO, 'Success sign up')
        return JsonResponse({'success': True, 'next': '/app',
                             'message': 'Success creation of new user'})
    return JsonResponse({'success': False,
                         'errors': signup_form.errors})


def app_view(request):
    return render(request, 'app.html')

