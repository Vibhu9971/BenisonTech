# Generated by Django 3.1.5 on 2021-01-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_utilisation', models.IntegerField()),
                ('device_status', models.CharField(choices=[('on', 'on'), ('off', 'off')], default='on', max_length=5)),
                ('memory_utilisation', models.IntegerField()),
            ],
        ),
    ]