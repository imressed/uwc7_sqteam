# -*- coding: utf-8 -*-
__author__ = 'imressed'

from django.utils import timezone
from rest_framework import serializers


class SqUserSerializer(serializers.Serializer):
    id = serializers.Field()
    email = serializers.EmailField()


class ProjectSerializer(serializers.Serializer):
    id = serializers.Field()
    name = serializers.CharField(max_length=100)
    topic = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    help_type = serializers.CharField(max_length=100)
    subscribers = SqUserSerializer(many=True, required=False)


class NewsSerializer(serializers.Serializer):
    id = serializers.Field()
    date = serializers.DateTimeField(default=timezone.now)
    text = serializers.CharField(max_length=200)
    #projects = ProjectSerializer(many=True, required=False)


