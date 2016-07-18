from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import LearnerProfile, InstructorProfile

from rest_framework.settings import import_from_string


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff',)


class LearnerProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer

    class Meta:
        model = LearnerProfile
        fields = ('id', 'user', 'active', 'instructor_profiles',)


class InstructorProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer
    learner_profiles = LearnerProfileSerializer(many=True)

    class Meta:
        model = InstructorProfile
        fields = ('id', 'user', 'active', 'learner_profiles',)

LearnerProfileSerializer._declared_fields['instructor_profiles'] = InstructorProfileSerializer(many=True)
