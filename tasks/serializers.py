from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login', 'date_joined', 'is_staff')


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')


	