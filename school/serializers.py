from rest_framework import serializers
from school.models import Student, Course, Registered
from school.validators import invalid_cpf, name_not_alpha, invalid_phone_number

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, values):
        if invalid_cpf(values['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter um valor válido'})

        if name_not_alpha(values['name']):
            raise serializers.ValidationError({'name': 'O nome deve contar somente letras'})

        if invalid_phone_number(values['phone_number']):
            raise serializers.ValidationError({'phone_number': 'O número de telefone precisar ter o modelo: 88 99999-9999'})

        return values

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registered
        exclude = []

class ListRegisteredStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registered
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()

class ListRegisteredCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registered
        fields = ['student_name']

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone_number']
