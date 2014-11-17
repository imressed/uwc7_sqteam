from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import HttpResponse, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import UserCreationForm


def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'index.html', {'login_form': login_form,
                                          'signup_form': signup_form})


@require_POST
def login_view(request):
    login_form = AuthenticationForm(data=request.POST)
    if login_form.is_valid():

        username = request.POST['username']
        password = request.POST['password']
        print('post data', username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('app')
            else:
                # Return a 'disabled account' error message
                return HttpResponse('Disabled account')
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('Invalid login')
    else:
        print(request.method, login_form.is_valid())
    return HttpResponse('Get login view')

def logout_view(request):
    logout(request)
    return redirect('index')

def signup_view(request):
    signup_form = UserCreationForm(data=request.POST)
    if request.method == 'POST' and signup_form.is_valid():
        signup_form.save()
        return redirect('index')
    return HttpResponse('Bad data')

@login_required
def app_view(request):
    return render(request, 'app.html')

