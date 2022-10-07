from email.policy import default
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    LEVELS = (
           ("Form1", "Form1"),
           ("Form 2", "Form2"),
           ("Form 3", "Form3"),
           ("Form 4", "Form4"),
    )
    level=models.CharField(max_length=10, choices=LEVELS)
    no_of_practicals =models.IntegerField(default=0)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.username, self.password)
 


class Teacher (models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=8)
    practicals = models.ForeignKey("Practical", on_delete=models.CASCADE, related_name="Teacher_practical", null=True)
    student = models.ForeignKey("Student",on_delete=models.CASCADE,related_name='Teacher_student', null=True )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name, self.username, self.email,self.student.first_name, self.student.last_name,self.practicals.title)
#  self.student.first_name, self.student.last_name,self.practicals.title
 

class Tool(models.Model):
    label = models.CharField(max_length=255, blank=True)
    image = models.ImageField()
    SUBJECTS = (
           ("Physics", "Physics"),
           ("Biology", "Biology"),
           ("Chemistry", "Chemistry"),
    )
    subject = models. CharField(max_length=20, choices=SUBJECTS)


class Practical(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=255)
    image = models.ImageField()
    instructions = models.TextField(max_length=255, blank=True)
    SUBJECTS = (
           ("Physics", "Physics"),
           ("Biology", "Biology"),
           ("Chemistry", "Chemistry"),
    )
    subject = models. CharField(max_length=20, choices=SUBJECTS)
    LEVELS = (
           ("Form1", "Form1"),
           ("Form 2", "Form2"),
           ("Form 3", "Form3"),
           ("Form 4", "Form4"),
    )
    level=models.CharField(max_length=10, choices=LEVELS)
    STATUS = (
           ("DONE", "Done"),
           ("Pending", "Pending"),
           ("Not done", "Not done"),
    )
    status = models.CharField(max_length=15, choices=STATUS)
    comments = models.BooleanField(default=False)
    video = models.FileField()
    observation = models.TextField(max_length=255, blank=True, null=True)
    time_date = models.DateTimeField(auto_now_add=True)
    comment_description = models.TextField(max_length=255, blank=True, null=True)
    tools = models.ForeignKey(Tool, on_delete=models.CASCADE,related_name='Tool_practical')





