from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from school.models import Registered
from school.serializers import RegisteredSerializer
import json

class RegisteredTestCase(APITestCase):
    fixtures = ["prototype_bd.json"]

    def setUp(self):
        self.user = User.objects.get(username="eduardo")
        self.url = reverse('registered-list')
        self.client.force_authenticate(self.user)

        # self.student_01 = Student.objects.get(
        #     name='Jonh 1',
        #     email='jonh1@gmail.com',
        #     cpf='916.289.550-82',
        #     date_of_birth='2023-02-02',
        #     phone_number='11 99999-9999'
        # )

        # self.student_02 = Student.objects.create(
        #     name='Jonh 2',
        #     email='jonh2@gmail.com',
        #     cpf='946.807.350-58',
        #     date_of_birth='2023-02-02',
        #     phone_number='11 99999-9999'
        # )

        self.course_01 = Course.objects.get(pk=1)
        self.course_02 = Course.objects.get(pk=2)
