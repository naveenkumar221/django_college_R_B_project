from django.db import models


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('Lab', 'Lab'),
        ('Seminar Hall', 'Seminar Hall'),
        ('Equipment', 'Equipment'),
    ]

    name = models.CharField(max_length=100)
    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPES
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Booking(models.Model):
    student_name = models.CharField(max_length=100)
    resource_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.student_name} - {self.resource_name}"
