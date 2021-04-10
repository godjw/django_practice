from django.contrib import admin
from .models import device, employee, work, checkpoint

admin.site.register(device)
admin.site.register(employee)
admin.site.register(work)
admin.site.register(checkpoint)