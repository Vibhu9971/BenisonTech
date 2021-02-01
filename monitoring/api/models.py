from django.db import models

# Create your models here.
DEVICE_STATUS_CHOICE = (
    ("on", "on"),
    ("off", "off")
    )

class DeviceLogs(models.Model):
    cpu_utilisation = models.IntegerField()
    device_status = models.CharField(max_length = 5, choices = DEVICE_STATUS_CHOICE, default = 'on')
    memory_utilisation = models.IntegerField()
