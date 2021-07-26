from django.db import models


# Create your models here.
class Spec(models.Model):
    special = models.CharField(primary_key=True, max_length=100)
    FOMO = models.CharField(max_length=50)

    def __str__(self):
        return self.special


class Prof(models.Model):
    prof = models.CharField(primary_key=True, max_length=100)
    description = models.TextField()
    specialisation = models.ForeignKey(Spec, on_delete=models.CASCADE, null=True, blank=True, db_column='special')

    def __str__(self):
        return f"{self.prof}"


class CourseContent(models.Model):
    ID = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    faculty = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, blank=True, db_column='prof')
    semester = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    course_credits = models.CharField(max_length=50)
    modality = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.ID} - {self.title}"

