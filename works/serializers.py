from rest_framework import serializers
from .models import Works


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'
        