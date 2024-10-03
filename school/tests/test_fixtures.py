from django.test import TestCase
from school.models import Student, Course

class FixtureTestCase(TestCase):
    fixtures = ["prototype_bd.json"]

    def test_get_fixtures(self):
        """Teste que verifica o carregamento das fixtures"""

        student = Student.objects.get(cpf="57528508004")
        course = Course.objects.get(pk=1)
        self.assertEqual(student.email,"mariagarcia@uol.com.br")
        self.assertEqual(course.code,"POO")
