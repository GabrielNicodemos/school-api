
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from school.views import StudentViewset, CourseViewset, RegisteredViewset, ListRegisteredStudentView, ListRegisteredCourseView

router = routers.DefaultRouter()
router.register('students', StudentViewset, basename="students")
router.register('cousers', CourseViewset, basename="cousers")
router.register('registered', RegisteredViewset, basename="registered")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('student/<int:pk>/registered', ListRegisteredStudentView.as_view()),
    path('course/<int:pk>/registered', ListRegisteredCourseView.as_view()),
]
