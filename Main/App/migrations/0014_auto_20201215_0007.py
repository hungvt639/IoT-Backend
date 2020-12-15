# Generated by Django 3.1.3 on 2020-12-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20201214_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='data',
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='App.sensordata')),
            ],
        ),
    ]
