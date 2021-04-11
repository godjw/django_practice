from django.db import models
from django.contrib.postgres.fields import array


class device(models.Model):
    device_id = models.CharField(primary_key=True, max_length=30)


class employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2)
    birth_date = models.DateField()


class checkpoint(models.Model):
    checkpoint_id = models.CharField(primary_key=True, max_length=30)
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    approval_status = models.BooleanField()


class time_gps(models.Model):
    time_gps_id = models.CharField(primary_key=True, max_length=30)
    time = models.DateTimeField()
    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)
    checkpoint_flag = models.BooleanField(default = False)
    checkpoint_id = models.ForeignKey(checkpoint, on_delete=models.PROTECT)


class work(models.Model):
    work_id = models.CharField(primary_key=True, max_length=30, default = "")
    device_info = models.ForeignKey(device, on_delete=models.PROTECT)
    employee_info = models.ForeignKey(employee, on_delete=models.PROTECT)
    work_start_time = models.DateTimeField()
    work_end_time = models.DateTimeField(null=True)
    approval_status = models.BooleanField(default=False)
    warning = models.BooleanField(default=False)
    time_and_gps = models.ManyToManyField(time_gps)

