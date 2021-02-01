from rest_framework import serializers
from .models import DeviceLogs

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLogs
        fields = ['id', "cpu_utilisation" ,"device_status","memory_utilisation"]
