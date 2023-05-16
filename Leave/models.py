from django.db import models

from Schoolapp.models import tbl_login

# Create your models here.

class leaveModel(models.Model):
    leave_choices = (
        ('FN', 'FN'),
        ('AN', 'AN'),
        ('FD', 'FD'),
        ('None', 'None'),
    )
    leaveId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    leaveDate = models.DateField()
    leaveDiv = models.CharField(max_length=10)
    leaveReason = models.CharField(max_length=50)
    leaveStatus = models.BooleanField('Approved', default=False)
    # type = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    # leaveRecords = models.FileField(upload_to="media/leave/")

    def __str__(self):
        return self.email.email


# Create your models here.
