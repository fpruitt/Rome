from django.contrib import admin

# Register your models here.
from accounts.models import LearnerProfile, InstructorProfile

admin.site.register(LearnerProfile)
admin.site.register(InstructorProfile)
