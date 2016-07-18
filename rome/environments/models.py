import uuid as uuid

from django.db import models
from accounts.models import LearnerProfile, InstructorProfile


class Lesson(models.Model):
    students = models.ManyToManyField(to=LearnerProfile, related_name="lessons")
    instructors = models.ManyToManyField(to=InstructorProfile, related_name="lessons")
    name = models.CharField(blank=True, default="", max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4)
    ue4_map_url = models.URLField(blank=True, default="")
