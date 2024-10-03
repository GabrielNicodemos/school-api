from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from school.models import Student
from school.serializers import StudentSerializer
import json


class StudentsTestCase(APITestCase):
    fixtures = ["prototype_bd.json"]

    def setUp(self):
        # self.user = User.objects.create_superuser(username='admin', password='admin')

        self.user = User.objects.get(username="eduardo")
        self.url = reverse('students-list')
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

        self.student_01 = Student.objects.get(pk=1)
        self.student_02 = Student.objects.get(pk=2)

    def test_request_get_list_students(self):
        """Teste de requisição GET"""

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_list_students_by_id(self):
        """Teste de requisição GET by ID"""

        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student_data = Student.objects.get(pk=1)
        student_data_serializers = StudentSerializer(instance=student_data).data
        self.assertEqual(response.data,student_data_serializers)

    def test_request_post_created_student(self):
        """Teste de requisição POST"""
        data_student = {
            'name': 'Vick',
            'email': 'vick@gmail.com',
            'cpf': '37091669002',
            'date_of_birth': '2022-03-03',
            'phone_number': '11 99999-9999'
        }

        response = self.client.post(self.url, data=json.dumps(data_student), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_student(self):
        """Teste de requisição DELETE"""
        data_student = {
            'name': 'Vick',
            'email': 'vick@gmail.com',
            'cpf': '370.916.690-02',
            'date_of_birth': '2022-03-03',
            'phone_number': '11 99999-9999'
        }

        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_request_put_update_student(self):
        """Teste de requisição PUT"""
        data_student = {
            'name': 'Lee',
            'email': 'lee@gmail.com',
            'cpf': '50447767003',
            'date_of_birth': '2020-02-01',
            'phone_number': '11 99999-8888'
        }

        response = self.client.put(f'{self.url}1/', data=json.dumps(data_student), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
