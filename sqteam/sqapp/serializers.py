# -*- coding: utf-8 -*-
__author__ = 'imressed'

from django.utils import timezone
from rest_framework import serializers
from .models import Project, SqUser, News


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'topic', 'location', 'help_type', 'subscribers')


class SqUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SqUser
        fields = ('id','email', 'projects')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'date', 'text', 'project')


