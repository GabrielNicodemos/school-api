from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from school.models import Student, Course, Registered
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    RegisteredSerializer,
    ListRegisteredStudentSerializer,
    ListRegisteredCourseSerializer,
    StudentSerializerV2
)
from rest_framework.throttling import UserRateThrottle
from school.throttling import RegisteredAnonRateThrottle



class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("id")
    # serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'cpf']
    ordering_fields = ['name']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer

class RegisteredViewset(viewsets.ModelViewSet):
    queryset = Registered.objects.all().order_by("id")
    serializer_class = RegisteredSerializer
    throttle_classes = [UserRateThrottle, RegisteredAnonRateThrottle]

class ListRegisteredStudentView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registered.objects.filter(student_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListRegisteredStudentSerializer


class ListRegisteredCourseView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Registered.objects.filter(course_id=self.kwargs['pk']).order_by("id")
        return queryset
    serializer_class = ListRegisteredCourseSerializer