from django.contrib.auth.models import User
from rest_framework import viewsets
from accounts.api.serializers import UserSerializer, InstructorProfileSerializer, LearnerProfileSerializer
from accounts.models import InstructorProfile, LearnerProfile


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer


class LearnerProfileViewSet(viewsets.ModelViewSet):
    queryset = LearnerProfile.objects.all()
    serializer_class = LearnerProfileSerializer
