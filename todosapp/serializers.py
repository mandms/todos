from rest_framework import serializers
from .models import Todos
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class TodosSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todos
        fields = ('name_of_todo', 'is_done', 'id', 'author')

class TodosDetailSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todos
        exclude = ('is_done', )

class TodosCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Todos
        fields = ('name_of_todo', 'description', 'deadline', 'author', 'id', 'is_done')
