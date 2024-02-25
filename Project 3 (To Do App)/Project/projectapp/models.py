from django.db import models

# Create your models here.


from django.db import models

class Task(models.Model):
    objects = None
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    name = models.TextField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=HIGH)
    task_date = models.DateField(default='1997-10-18')

    def __str__(self):
        return self.name

