from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    status = models.BooleanField(default=False)


class Type_Equipment(models.Model):
    name = models.CharField(max_length=55)


class StatusOrder(models.Model):
    name = models.CharField(max_length=55)


class Priority(models.Model):
    name = models.CharField(max_length=20)


class Equipment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    type_equipment = models.ForeignKey(Type_Equipment, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=255)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateTimeField()
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    description = models.TextField()


class materials(models.Model):
    name = models.CharField(max_length=55)


class used_materials(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_material = models.ForeignKey(materials, on_delete=models.CASCADE)
    quantity = models.IntegerField()