from django.test import TestCase
from Varsity_Admin.models import *
from Student.models import *
from Hall_Admin.models import *
from Provost.models import *
class StudentModelTestCase(TestCase):
    def setUp(self):
        admin=HallAdmin.objects.create(adminId=11,email='admin@gmail.com',username='admin',password='aa')
        provost=Provost.objects.create(provostId=12,email='provost@gmail.com',username='provost',password='aa')
        self.hall = Hall.objects.create(hallId=1, name="Test Hall",hallAdmin=admin,provost=provost)
        self.room = Room.objects.create(roomId=1, hall=self.hall)
        self.session = Session.objects.create(session=1)
        self.student = Student.objects.create(
            studentId=1,
            name="Test Student",
            email="test@example.com",
            username="test_username",
            password="test_password",
            hall=self.hall,
            session=self.session,
            room=self.room,
            studentType="Undergraduate"
        )

    def test_student_creation(self):
        self.assertEqual(self.student.studentId, 1)
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.email, "test@example.com")
        self.assertEqual(self.student.username, "test_username")
        self.assertEqual(self.student.password, "test_password")
        self.assertEqual(self.student.hall, self.hall)
        self.assertEqual(self.student.session, self.session)
        self.assertEqual(self.student.room, self.room)
        self.assertEqual(self.student.studentType, "Undergraduate")
    def test_student_str_representation(self):
        self.assertEqual(str(self.student), "Test Student - 1")
    def test_student_deletion(self):
        student_count_before_delete = Student.objects.count()
        self.student.delete()
        student_count_after_delete = Student.objects.count()
        self.assertEqual(student_count_before_delete - 1, student_count_after_delete)