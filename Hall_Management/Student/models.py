from Varsity_Admin.models import Hall, Room
from django.db import models


class Session(models.Model):
    """
    Model representing a session.

    A session represents a specific academic term or period.

    Attributes:
        session (int): The session number.
        csvFile (FileField): The CSV file associated with this session.
    """

    session = models.IntegerField(default=0, null=True, blank=True)
    csvFile = models.FileField(upload_to='csvs/', null=True, blank=True)

    def __str__(self):
        """String representation of the session."""
        return str(self.session)


class Student(models.Model):
    """
    Model representing a student.

    A student is a person enrolled in a particular session, hall, and room.

    Attributes:
        studentId (int): The unique identifier for the student.
        name (str): The name of the student.
        email (str): The email address of the student.
        username (str): The username of the student.
        password (str): The password of the student.
        hall (ForeignKey): The hall the student belongs to.
        session (ForeignKey): The session the student is enrolled in.
        room (ForeignKey): The room the student is assigned to.
        studentType (str): The type of student (e.g., undergraduate, graduate).
    """

    studentId = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    studentType = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String representation of the student."""
        return f"{self.name} - {self.studentId}"


class SwapRequest(models.Model):
    """
    Model representing a swap request made by a student.

    Attributes:
        student (ForeignKey): The student making the swap request.
        reason (str): The reason for the swap request.
        status (int): The status of the swap request (0 for pending, 1 for accepted, 2 for rejected).
        noOfRequests (int): The number of swap requests made by the student.
        hall (ForeignKey): The hall associated with the swap request.
    """

    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200, null=True)
    status = models.IntegerField(default=0, null=True)
    noOfRequests = models.IntegerField(default=0, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """String representation of the swap request."""
        return f"{self.student.studentId} - {self.hall.hallId}"


class RepairRequest(models.Model):
    """
    Model representing a repair request made by a student.

    Attributes:
        requestId (int): The unique identifier for the repair request.
        student (ForeignKey): The student making the repair request.
        reason (str): The reason for the repair request.
        status (int): The status of the repair request (0 for pending, 1 for completed).
        hall (ForeignKey): The hall associated with the repair request.
        requestType (int): The type of repair request.
        date (str): The date when the repair request was made.
    """

    requestId = models.IntegerField(default=0, null=True)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200, null=True)
    status = models.IntegerField(default=0, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)
    requestType = models.IntegerField(default=0, null=True)
    date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String representation of the repair request."""
        return f"{self.student.studentId} - {self.hall.hallId}"