from django.contrib import admin
from .models import Client, Worker, Type_Equipment, StatusOrder, Priority, Equipment, Order, materials, used_materials

admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Type_Equipment)
admin.site.register(StatusOrder)
admin.site.register(Priority)
admin.site.register(Equipment)
admin.site.register(Order)
admin.site.register(materials)
admin.site.register(used_materials)
