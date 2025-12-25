from rest_framework import serializers
from .models import Task, Category
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # only show owner username

    class Meta:
        model = Category
        fields = '__all__'