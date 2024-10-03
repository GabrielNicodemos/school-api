from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from school.models import Course
from school.serializers import CourseSerializer
import json

class CourseTestCase(APITestCase):
    fixtures = ["prototype_bd.json"]

    def setUp(self):
        self.user = User.objects.get(username="eduardo")
        self.url = reverse('cousers-list')
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

    def test_request_get_list_course(self):
        """Teste de requisição GET"""

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_list_course_by_id(self):
        """Teste de requisição GET by ID"""

        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        course_data = Course.objects.get(pk=1)
        course_data_serializers = CourseSerializer(instance=course_data).data
        self.assertEqual(response.data,course_data_serializers)

    def test_request_post_created_course(self):
        """Teste de requisição POST"""
        data_course = {
            'code': 'XPTX',
            'description': 'Curso XPTZ',
            'level': 'B',
        }

        response = self.client.post(self.url, data=json.dumps(data_course), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_course(self):
        """Teste de requisição DELETE"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_request_put_update_course(self):
        """Teste de requisição PUT"""
        data_course = {
            'code': 'XPTT',
            'description': 'Curso XPTT',
            'level': 'A',
        }

        response = self.client.put(f'{self.url}1/', data=json.dumps(data_course), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)