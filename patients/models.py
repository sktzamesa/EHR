from django.db import models
from account.models import Profile
from doctor.models import Doctor
# Create your models here.
class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    birth_date = models.DateField()
    medical_history = models.TextField(blank=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')

    def __str__(self):
        return self.profile.user.get_full_name()