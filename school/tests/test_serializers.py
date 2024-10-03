from django.test import TestCase
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    RegisteredSerializer
)
from school.models import Student, Course, Registered


class SerializerStudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name='Jonh',
            email='jonh@gmail.com',
            cpf='712.004.100-25',
            date_of_birth='2023-02-02',
            phone_number='11 99999-9999'
        )

        self.serializer_student = StudentSerializer(instance=self.student)

    def test_verify_student_serializers_fields(self):
        """Teste que verifica os campos que estão sendo serializados de estudante"""
        data = self.serializer_student.data

        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'cpf', 'date_of_birth', 'phone_number']))

    def test_verify_content_student_serializers_fields(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de estudante"""
        data = self.serializer_student.data

        self.assertEqual(data['name'], self.student.name)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cpf'], self.student.cpf)
        self.assertEqual(data['date_of_birth'], self.student.date_of_birth)
        self.assertEqual(data['phone_number'], self.student.phone_number)

class SerializerCourseTestCase(TestCase):
    def setUp(self):
        self.course = Course(
            code='XPTO',
            description='Curso XPTO',
            level='Basic',
        )

        self.serializer_course = CourseSerializer(instance=self.course)

    def test_verify_course_serializers_fields(self):
        """Teste que verifica os campos que estão sendo serializados de um curso"""
        data = self.serializer_course.data

        self.assertEqual(set(data.keys()), set(['id', 'code', 'description', 'level']))

    def test_verify_content_course_serializers_fields(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de um curso"""
        data = self.serializer_course.data

        self.assertEqual(data['code'], self.course.code)
        self.assertEqual(data['description'], self.course.description)
        self.assertEqual(data['level'], self.course.level)

class RegisteredSerializerTestCase(TestCase):
    def setUp(self):
        # Cria e salva o curso no banco de dados
        self.course = Course.objects.create(
            code='XPTO',
            description='Curso XPTO',
            level='Basic',
        )

        # Cria e salva o estudante no banco de dados
        self.student = Student.objects.create(
            name='Jonh',
            email='jonh@gmail.com',
            cpf='712.004.100-25',
            date_of_birth='2023-02-02',
            phone_number='11 99999-9999'
        )

        self.registered = Registered(
            student=self.student,
            course=self.course,
            period='Morning',
        )


        self.serializer_registered = RegisteredSerializer(instance=self.registered)

    def test_verify_course_serializers_fields(self):
        """Teste que verifica os campos que estão sendo serializados de um curso"""
        data = self.serializer_registered.data

        self.assertEqual(set(data.keys()), set(['id', 'student', 'course', 'period']))

    def test_verify_content_course_serializers_fields(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de um curso"""
        data = self.serializer_registered.data

        self.assertEqual(data['student'], self.registered.student.id)
        self.assertEqual(data['course'], self.registered.course.id)
        self.assertEqual(data['period'], self.registered.period)