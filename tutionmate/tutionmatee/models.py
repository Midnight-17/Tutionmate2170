from django.db import models

class subjects(models.Model):
    type = models.CharField(max_length=100)


    def __str__(self):
        return self.type

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(subjects, related_name="subjects")
    age = models.IntegerField(null=True, blank= True)

    def __str__(self):
        return self.name