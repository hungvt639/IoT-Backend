# Generated by Django 3.1.3 on 2020-12-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20201213_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='data',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]