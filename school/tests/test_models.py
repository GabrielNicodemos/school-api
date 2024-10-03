from django.test import TestCase
from school.models import Student, Course, Registered


class BaseTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name='Jonh',
            email='jonh@gmail.com',
            cpf='712.004.100-25',
            date_of_birth='2023-02-02',
            phone_number='11 99999-9999'
        )

        self.course = Course.objects.create(
            code='XPTO',
            description='Curso XPTO',
            level='Basic',
        )

class ModelStudentTestCase(BaseTestCase):
    def test_verify_create_student(self):
        """Teste que verifica a criação de um estudante e seus atributos"""
        self.assertEqual(self.student.name, 'Jonh')
        self.assertEqual(self.student.email, 'jonh@gmail.com')
        self.assertEqual(self.student.cpf, '712.004.100-25')
        self.assertEqual(self.student.date_of_birth, '2023-02-02')
        self.assertEqual(self.student.phone_number, '11 99999-9999')

class ModelCourseTestCase(BaseTestCase):
    def test_verify_create_student(self):
        """Teste que verifica a criação de um curso e seus atributos"""
        self.assertEqual(self.course.code, 'XPTO')
        self.assertEqual(self.course.description, 'Curso XPTO')
        self.assertEqual(self.course.level, 'Basic')

class ModelRegisteredTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.registered = Registered.objects.create(
            student=self.student,
            course=self.course,
            period='Morning',
        )

    def test_verify_create_registered(self):
        """Teste que verifica a criação de um matrícula e seus atributos"""
        self.assertEqual(self.registered.student, self.student)
        self.assertEqual(self.registered.course, self.course)
        self.assertEqual(self.registered.period, 'Morning')
