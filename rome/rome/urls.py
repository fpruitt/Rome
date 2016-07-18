from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from accounts.api.viewsets import UserViewSet, LearnerProfileViewSet, InstructorProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', LearnerProfileViewSet)
router.register(r'instructors', InstructorProfileViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
