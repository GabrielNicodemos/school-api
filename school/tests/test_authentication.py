from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('students-list')

    def test_authentication_user_correct_credentials(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and (user.is_authenticated))

    def test_authentication_user_incorrect_credentials(self):
        """Teste que verifica a autenticação de um user com as credenciais incorretas"""

        # With username incorrect
        user = authenticate(username='admin111', password='admin')
        self.assertFalse((user is not None) and (user.is_authenticated))

        # With password incorrect
        user = authenticate(username='admin', password='admin1111')
        self.assertFalse((user is not None) and (user.is_authenticated))

    def test_request_get_test_request_get_authorized(self):
        """Verifica uma requisição GET autorizada"""

        # Forçar Autenticação
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_unauthorized(self):
        """Verifica uma requisição GET não autorizada autorizada"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)