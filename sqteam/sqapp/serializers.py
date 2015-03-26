# -*- coding: utf-8 -*-
__author__ = 'imressed'

from django.utils import timezone
from rest_framework import serializers
from .models import Project, SqUser, News


class SqUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SqUser
        fields = ('id','email', 'projects')


#class ProjectSerializer(serializers.Serializer):
#    id = serializers.Field()
#    name = serializers.CharField(max_length=100)
#    topic = serializers.CharField(max_length=100)
#    location = serializers.CharField(max_length=100)
#    help_type = serializers.CharField(max_length=100)
#    subscribers = SqUserSerializer(many=True, required=False)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'topic', 'location', 'help_type', 'subscribers')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'date', 'text', 'project')


