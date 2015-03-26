import json

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.shortcuts import HttpResponse, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import (require_http_methods, require_POST,
                                          require_GET)
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import pre_save

from .forms import UserCreationForm
from .models import Project, News, SqUser
from .serializers import ProjectSerializer, NewsSerializer, SqUserSerializer

from django.contrib import messages


class SqUserViewSet(viewsets.ViewSet):
    model = SqUser

    def list(self, request):
        queryset = SqUser.objects.all()
        serializer = SqUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SqUser.objects.all()
        user = queryset.get(id=pk)
        serializer = SqUserSerializer(user, many=False)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ViewSet):
    model = Project

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = queryset.get(id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)


class NewsViewSet(viewsets.ViewSet):
    model = News

    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.all()
        news = queryset.get(id=pk)
        serializer = NewsSerializer(news, many=False)
        return Response(serializer.data)



def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'index_new.html', {'login_form': login_form,
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
            return JsonResponse({'success': True,
                                 'message': 'Success login'})
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


@login_required
def subscribe(request, project_id):
    pr = get_object_or_404(Project, pk=int(project_id))
    user = request.user
    pr.subscribers.add(user)
    return JsonResponse({
        'success': True,
        'message': u'User {0} has been subscribed to the {1}'.format(user.email, pr.name)
    })

def search(request):
    search_fields = ('help_type', 'location', 'topic')
    projects = Project.objects.all()
    for sf in search_fields:
        value = request.GET.get(sf, '')
        params = {sf: value}
        if value:
            projects = projects.filter(**params)

    return JsonResponse([p.serialize() for p in projects], safe=False)

#todo: for the sake of simplicity just use finished serializer instead of these two views
def get_news(request, project_id):

    news = News.objects.filter(project=project_id)

    return JsonResponse([n.serialize() for n in news], safe=False)


@receiver(pre_save)
def deliver_mails(sender, instance, *args, **kwargs):
    if isinstance(instance, News):
        subs = instance.project.subscribers.all()
        for s in subs:
            print(s.email)


