from .models import MyUsers
from django.contrib.auth.models import Group, Permission


def createGroup():
    new_group, created = Group.objects.get_or_create(name='admin')
    perm = Permission.objects.all()
    new_group.permissions.set(perm)

    new_group, created = Group.objects.get_or_create(name='user')
    perm = [
        Permission.objects.get(codename='view_chip'),
        Permission.objects.get(codename='add_chip'),
        Permission.objects.get(codename='change_chip'),
        Permission.objects.get(codename='delete_chip'),

        Permission.objects.get(codename='view_devicesensor'),
        Permission.objects.get(codename='add_devicesensor'),
        Permission.objects.get(codename='change_devicesensor'),
        Permission.objects.get(codename='delete_devicesensor'),

        Permission.objects.get(codename='view_devicedata'),
        Permission.objects.get(codename='add_devicedata'),


        Permission.objects.get(codename='view_sensordata'),
        Permission.objects.get(codename='add_sensordata'),

        Permission.objects.get(codename='view_command'),
        Permission.objects.get(codename='add_command'),
    ]
    new_group.permissions.set(perm)


def user_permission(id, perm):
    user = MyUsers.objects.get(pk=id)
    user.groups.add(Group.objects.get(name=perm))