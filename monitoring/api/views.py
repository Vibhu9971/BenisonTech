from django.shortcuts import render
from .serializers import LogSerializer
from rest_framework import generics
from .models import DeviceLogs
from django.conf import settings
from django.core.mail import send_mail
import smtplib
# Create your views here.
class Logs(generics.ListCreateAPIView):
    queryset = DeviceLogs.objects.all()
    serializer_class = LogSerializer

    def perform_create(self, serializer):
        serializer.save()
        device_details = serializer.data
        threshold = 400
        alarm = 0

        if device_details['device_status'] == "off":
            subject = "Device is down"
            body = "Device with CPU utilisation %d and memory utilisation %d is off, please check and update the database"% (device_details['cpu_utilisation'], device_details['memory_utilisation'])
            alarm = 1
        elif device_details['cpu_utilisation'] > threshold:
            subject = "CPU Utilisation is greater than threshold"
            body = "CPU Utilisation %d is greater than threshold %d"% (device_details['cpu_utilisation'], threshold)
            alarm = 1
        if alarm:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login("vibhutr1993@gmail.com", "tebfbdflqumgqexs")
            msg = f"Subject: {subject}\n\n{body}"
            server.sendmail("vibhutr1993@gmail.com", "vibhu.yash82@gmail.com", msg)
            server.quit()
