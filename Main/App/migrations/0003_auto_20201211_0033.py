# Generated by Django 3.1.3 on 2020-12-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20201211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chip',
            name='key',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
