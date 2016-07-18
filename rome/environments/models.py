import uuid as uuid

from django.db import models
from accounts.models import LearnerProfile, InstructorProfile


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Language: {name}".format(name=self.name)


class Lesson(models.Model):
    students = models.ManyToManyField(to=LearnerProfile, related_name="lessons", blank=True)
    instructors = models.ManyToManyField(to=InstructorProfile, related_name="lessons", blank=True)
    name = models.CharField(blank=True, default="", max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4)
    ue4_map_url = models.URLField(blank=True, default="")
    target_language = models.ForeignKey(to=Language, related_name="lessons", null=True, blank=True)

    def __str__(self):
        return "Lesson: {name} in language {language}".format(name=self.name, language=self.target_language.name)
