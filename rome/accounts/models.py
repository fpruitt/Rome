from django.contrib.auth.models import User
from django.db import models


class LearnerProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='learner_profile')
    active = models.BooleanField(default=True)


class InstructorProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='instructor_profile')
    active = models.BooleanField(default=True)
    student_profiles = models.ManyToManyField(to=LearnerProfile, related_name='instructor_profiles')
